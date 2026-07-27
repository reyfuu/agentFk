# AI Agent Riset News FK

Agent riset berita AI harian untuk Freddie Kashawan. Repository ini berisi
prompt riset, referensi persona, scheduled task Claude Desktop, dan arsip output.

## Status

Workflow yang tersedia saat ini berjalan melalui Claude Desktop:

1. Riset maksimal 10 berita AI terbaru.
2. Membuat brief untuk setiap berita.
3. Membuat tiga versi script Reels per berita.
4. Menyimpan output lokal dan mengunggahnya ke Google Drive.

Repository ini belum memiliki runner headless. Artinya, clone ke GitHub atau VPS
belum otomatis membuat scheduled task berjalan.

## Menjalankan versi saat ini

Ikuti [SETUP GUIDE.md](SETUP%20GUIDE.md) untuk memasang skill dan scheduled task
di Claude Desktop.

## Rencana GitHub dan VPS

Lihat [DEPLOYMENT.md](DEPLOYMENT.md) untuk rancangan migrasi. Rekomendasi awal
adalah membuat satu runner sederhana yang bisa dipanggil oleh cron di VPS.
GitHub Actions dapat dipakai untuk pengujian dan pemicu manual setelah runner
tersebut tersedia.

## Output

Hasil harian disimpan di folder `Riset AI News`:

- `YYYY-MM-DD.md` untuk brief berita.
- `YYYY-MM-DD (Script).md` untuk script Reels.

