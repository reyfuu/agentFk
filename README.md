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

## Menjalankan di GitHub Actions

1. Buka repository GitHub, lalu `Settings`, `Secrets and variables`, `Actions`.
2. Tambahkan repository secret bernama `ANTHROPIC_API_KEY`.
3. Buka tab `Actions`, pilih `Run AI News`, lalu klik `Run workflow`.
4. Setelah selesai, unduh artifact `ai-news-...` dari halaman run.

Workflow produksi hanya berjalan manual. Push dan pull request menjalankan
self-check tanpa memakai API. Hasil run disimpan sebagai artifact selama 14
hari dan tidak otomatis di-commit atau diunggah ke Google Drive.

Model default adalah `claude-sonnet-4-6`. Untuk menggantinya, buat repository
variable `CLAUDE_MODEL`. Jika variable tidak dibuat, runner memakai model
default.

## Rencana VPS

Lihat [DEPLOYMENT.md](DEPLOYMENT.md) untuk tahap berikutnya setelah hasil
GitHub Actions stabil.

## Output

Hasil harian disimpan di folder `Riset AI News`:

- `YYYY-MM-DD.md` untuk brief berita.
- `YYYY-MM-DD (Script).md` untuk script Reels.
