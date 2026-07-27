# AI Agent Riset News FK — Setup Guide

Panduan instalasi untuk PC baru. Ikuti langkah-langkah di bawah secara berurutan.

---

## Prasyarat

Pastikan sudah terinstall:
- Claude Desktop (download di claude.ai)
- Akun Claude dengan subscription aktif (Pro atau lebih)
- Koneksi Google Drive aktif di Claude (untuk push output otomatis)

---

## Langkah 1 — Copy Skill

Salin folder skill ke direktori Claude:

DARI:
  AI Agent Riset News FK\skills\ai-news-riset-fk\

KE:
  C:\Users\[nama_user]\.claude\skills\ai-news-riset-fk\

Jika folder skills belum ada di dalam .claude, buat dulu foldernya.

---

## Langkah 2 — Buat Folder Output

Buat folder untuk menyimpan hasil riset harian:

  C:\Users\[nama_user]\AI Agent Riset News FK\Riset AI News\

Atau letakkan folder AI Agent Riset News FK di lokasi yang kamu inginkan, lalu sesuaikan path di Langkah 3.

---

## Langkah 3 — Sesuaikan Path Output

Buka file berikut dan ganti semua [USERNAME] dengan username Windows kamu:

  AI Agent Riset News FK\scheduled-tasks\daily-script-news-fk\SKILL.md

Dua baris yang perlu diganti:
  C:\Users\[USERNAME]\AI Agent Riset News FK\Riset AI News\YYYY-MM-DD.md
  C:\Users\[USERNAME]\AI Agent Riset News FK\Riset AI News\YYYY-MM-DD (Script).md

Ganti menjadi path sesuai lokasi folder di PC kamu.

---

## Langkah 4 — Setup Scheduled Task

Buka Claude Desktop, lalu ketik di chat:

  "Buatkan scheduled task dari konten file ini setiap hari jam 12 malam"

Lalu paste seluruh isi file:
  AI Agent Riset News FK\scheduled-tasks\daily-script-news-fk\SKILL.md

Claude akan membuat scheduled task baru dengan nama "Daily Script+News FK" dan jadwal harian jam 00:00.

---

## Langkah 5 — Pre-Approve Tool Permissions

Setelah scheduled task dibuat, klik Run Now sekali untuk menjalankan secara manual.

Saat diminta izin, approve semua tool berikut:
- WebSearch
- WebFetch
- create_file (Google Drive)
- Read, Write (untuk file lokal)

Setelah diapprove sekali, izin tersimpan dan run otomatis berikutnya tidak akan minta izin lagi.

---

## Cara Pakai

OTOMATIS (via Scheduled Task):
Berjalan setiap hari jam 00:00 waktu lokal.
Output muncul di Claude Desktop sebagai sesi baru saat app dibuka.
Catatan: Claude Desktop harus dalam keadaan terbuka agar scheduled task berjalan.

MANUAL (kapan saja):
Ketik di Claude: "riset news FK" atau "jalankan riset AI news"
Claude akan langsung menjalankan seluruh workflow.

---

## Output yang Dihasilkan Per Hari

Dua file lokal:
  Riset AI News\YYYY-MM-DD.md                 (10 berita brief)
  Riset AI News\YYYY-MM-DD (Script).md         (30 script Reels)

Dua file di Google Drive (folder ID: 1Xs_z5CRpxoW857H764Up0L1O8p4clY0x):
  "Riset AI News, DD Month YYYY"
  "Riset AI News (Script), DD Month YYYY"

---

## Struktur Script Output

Setiap malam menghasilkan 30 script dari 10 berita dikali 3 persona:
- RAYMOND CHIN: framing bisnis dan peluang, storytelling kasus nyata
- TIMOTHY RONALD: framing values dan growth jangka panjang, filosofis
- ANDREAS: framing builder dan AI tools, technical review

Setiap script terdiri dari: HOOK, SCRIPT, CTA, CAPTION, HASHTAG
Platform: Instagram Reels dan TikTok
Durasi: 30 sampai 60 detik per script

---

## Google Drive

Folder tujuan: https://drive.google.com/drive/folders/1Xs_z5CRpxoW857H764Up0L1O8p4clY0x
Folder ID: 1Xs_z5CRpxoW857H764Up0L1O8p4clY0x

Jika ingin mengganti folder Drive, update parentId di:
  scheduled-tasks\daily-script-news-fk\SKILL.md (Step 7 dan Step 10)
  .claude\scheduled-tasks\daily-script-news-fk\SKILL.md (yang sudah terinstall)

---

## Troubleshooting

Skill tidak terdeteksi:
Pastikan path sudah benar: .claude\skills\ai-news-riset-fk\SKILL.md

Scheduled task berhenti minta izin:
Klik Run Now sekali untuk pre-approve semua tool, baru biarkan jalan otomatis.

Output tidak muncul:
Pastikan Claude Desktop app terbuka saat jadwal berjalan jam 00:00.

File lokal tidak tersimpan:
Cek path output di SKILL.md scheduled task, pastikan folder Riset AI News sudah ada dan path sudah benar untuk username kamu.

Drive push gagal:
Output akan muncul di chat untuk di-copy manual. Cek koneksi Google Drive di pengaturan Claude Desktop.
