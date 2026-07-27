# AI Agent Riset News FK

Working directory untuk AI Agent riset berita AI harian milik Freddie Kashawan (AIpreneur).

## Tujuan

Agent ini menjalankan riset berita AI setiap malam — fetch dari 50+ sumber resmi dan kreator AI, filter 10 berita terbaik, tulis brief siap-pakai, generate 30 script Reels (3 persona x 10 berita), lalu push dua output ke Google Drive.

Output digunakan sebagai bahan baku konten Instagram Reels dan TikTok akun Freddie Kashawan AIpreneur.

## Struktur Folder

```
AI Agent Riset News FK/
├── SETUP GUIDE.md                           portability guide untuk PC baru
├── CLAUDE.md                                file ini, project context
├── SKILL.md                                 skill reference lengkap (source of truth)
├── skills/
│   └── ai-news-riset-fk/
│       └── SKILL.md                         copy untuk instalasi ke .claude\skills\
├── scheduled-tasks/
│   └── daily-script-news-fk/          (nama routine: Daily Script+News FK)
│       └── SKILL.md                         prompt self-contained untuk scheduled task
├── Riset AI News/                           output harian
│   ├── README.md
│   ├── YYYY-MM-DD.md                        brief harian
│   └── YYYY-MM-DD (Script).md              script pack harian
├── Raymond.txt                              referensi gaya Raymond Chin
├── Timothy.txt                              referensi gaya Timothy Ronald
└── Andreas.txt                              referensi gaya Andreas
```

## Cara Kerja

Scheduled task berjalan setiap malam jam 00:00. Saat aktif:
1. Riset 10 berita AI terbaru dari 50+ sumber
2. Tulis brief panjang per berita (Ringkasan + Why It Matters)
3. Push brief ke Drive: "Riset AI News, DD Month YYYY"
4. Generate 30 script Reels (Raymond, Timothy, Andreas x 10 berita)
5. Push script ke Drive: "Riset AI News (Script), DD Month YYYY"

## Google Drive

Folder ID: 1Xs_z5CRpxoW857H764Up0L1O8p4clY0x
Link: https://drive.google.com/drive/folders/1Xs_z5CRpxoW857H764Up0L1O8p4clY0x

## Pindah ke PC Baru

Lihat SETUP GUIDE.md untuk panduan lengkap instalasi di PC baru.
Langkah utama: copy skills folder, update path username di scheduled task SKILL.md, buat ulang scheduled task di Claude Desktop.
