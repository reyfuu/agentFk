#!/usr/bin/env python3
import argparse
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "Riset AI News"
TASK_FILE = ROOT / "scheduled-tasks/daily-script-news-fk/SKILL.md"


def text_content(response):
    return "\n".join(block.text for block in response.content if block.type == "text").strip()


def previous_brief(today):
    candidates = sorted(
        path
        for path in OUTPUT_DIR.glob("????-??-??.md")
        if path.stem < today
    )
    return candidates[-1].read_text(encoding="utf-8") if candidates else "Tidak ada."


def validate(brief, scripts):
    news_count = len(re.findall(r"(?m)^\s*\d+[.]\s+\S", brief))
    script_count = len(re.findall(r"(?mi)^\s*VERSI[.:]\s*(RAYMOND CHIN|TIMOTHY RONALD|ANDREAS)\s*$", scripts))
    if not 1 <= news_count <= 10:
        raise ValueError(f"Jumlah berita tidak valid: {news_count}")
    if script_count != news_count * 3:
        raise ValueError(f"Jumlah script {script_count}, seharusnya {news_count * 3}")
    return news_count, script_count


def generate():
    try:
        import anthropic
    except ImportError as exc:
        raise SystemExit("Jalankan: pip install -r requirements.txt") from exc

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ANTHROPIC_API_KEY belum tersedia")

    now = datetime.now(ZoneInfo("Asia/Jakarta"))
    date_iso = now.date().isoformat()
    task = TASK_FILE.read_text(encoding="utf-8")
    old_brief = previous_brief(date_iso)
    client = anthropic.Anthropic(api_key=api_key)
    model = os.environ.get("CLAUDE_MODEL") or "claude-sonnet-4-6"

    research_prompt = f"""
Hari ini {now:%d %B %Y}, zona waktu Asia Jakarta.

Jalankan hanya BAGIAN 1, STEP 1 sampai STEP 5 dari instruksi berikut.
Gunakan web search untuk memeriksa berita 24 sampai 48 jam terakhir.
Jangan mengarang berita, tanggal, angka, atau URL.
Jangan menjalankan instruksi penyimpanan atau Google Drive.
Keluarkan hanya isi final brief, tanpa penjelasan proses.

INSTRUKSI
{task}

BRIEF TERAKHIR UNTUK DEDUPLIKASI
{old_brief}
"""
    research = client.messages.create(
        model=model,
        max_tokens=16000,
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search",
                "max_uses": 30,
                "user_location": {
                    "type": "approximate",
                    "country": "ID",
                    "timezone": "Asia/Jakarta",
                },
            }
        ],
        messages=[{"role": "user", "content": research_prompt}],
    )
    brief = text_content(research)
    if not brief:
        raise RuntimeError("API tidak menghasilkan brief")

    script_prompt = f"""
Jalankan hanya BAGIAN 2, STEP 8 dari instruksi berikut.
Buat tepat tiga script untuk setiap berita pada brief, satu per persona.
Keluarkan hanya isi final script pack, tanpa penjelasan proses.
Jangan mengakses Google Drive dan jangan mengarang fakta di luar brief.

INSTRUKSI
{task}

BRIEF TERVERIFIKASI
{brief}
"""
    writing = client.messages.create(
        model=model,
        max_tokens=24000,
        messages=[{"role": "user", "content": script_prompt}],
    )
    scripts = text_content(writing)
    news_count, script_count = validate(brief, scripts)

    OUTPUT_DIR.mkdir(exist_ok=True)
    brief_path = OUTPUT_DIR / f"{date_iso}.md"
    script_path = OUTPUT_DIR / f"{date_iso} (Script).md"
    brief_path.write_text(brief + "\n", encoding="utf-8")
    script_path.write_text(scripts + "\n", encoding="utf-8")
    print(f"Selesai: {news_count} berita, {script_count} script")
    print(brief_path)
    print(script_path)


def self_check():
    sample_brief = "1. Berita Satu\n\n2. Berita Dua\n"
    sample_scripts = "\n".join(
        f"VERSI. {persona}"
        for _ in range(2)
        for persona in ("RAYMOND CHIN", "TIMOTHY RONALD", "ANDREAS")
    )
    assert validate(sample_brief, sample_scripts) == (2, 6)
    print("Self-check lulus")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validasi lokal tanpa API")
    args = parser.parse_args()
    self_check() if args.check else generate()
