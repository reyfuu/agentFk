# Brainstorming Deployment GitHub dan VPS

## Kondisi sekarang

Isi repository adalah prompt dan data referensi. Eksekusinya masih bergantung
pada Claude Desktop, WebSearch, WebFetch, akses file lokal, dan koneksi Google
Drive milik aplikasi desktop.

Karena belum ada program runner, repository ini belum dapat dijalankan langsung
oleh GitHub Actions atau cron di VPS.

## Target minimum

Satu perintah berikut harus dapat menjalankan workflow tanpa antarmuka desktop:

```bash
python run.py
```

Runner minimum bertanggung jawab untuk:

1. Membaca prompt utama dan output hari sebelumnya.
2. Memanggil model yang mendukung pencarian web.
3. Memvalidasi serta menyimpan brief dan script ke `Riset AI News`.
4. Mengunggah dua output ke Google Drive.
5. Mengembalikan exit code nonzero jika proses gagal.

## Rekomendasi arsitektur

Gunakan satu proses Python, satu file konfigurasi environment, dan cron bawaan
Linux. Hindari database, queue, Docker, dan dashboard sampai kebutuhan nyata
muncul.

```text
cron
  |
  v
run.py -> API model dan web search
  |
  +-> Riset AI News
  |
  +-> Google Drive API
```

Environment yang kemungkinan dibutuhkan:

```text
ANTHROPIC_API_KEY
GOOGLE_DRIVE_FOLDER_ID
GOOGLE_SERVICE_ACCOUNT_JSON
TZ=Asia/Jakarta
```

Nama dan format credential final harus mengikuti provider yang dipilih saat
runner mulai dibuat. Jangan commit file `.env` atau credential Google.

## Pilihan scheduler

### VPS cron, direkomendasikan

Kelebihan:

- Zona waktu dan jadwal lebih mudah dikontrol.
- File output dapat disimpan persisten.
- Lebih cocok untuk proses riset yang durasinya tidak selalu sama.

Kekurangan:

- Server perlu dipelihara.
- Log rotation dan alert kegagalan perlu disiapkan.

### GitHub Actions

Kelebihan:

- Tidak perlu mengelola server.
- Riwayat run dan log tersedia di GitHub.

Kekurangan:

- Secret Google dan API harus disimpan di GitHub Secrets.
- Output lokal hilang setelah job selesai kecuali diunggah atau di-commit.
- Schedule bukan pilihan ideal bila waktu eksekusi harus sangat presisi.

## Tahapan implementasi

### Fase 1, runner lokal

- Ekstrak instruksi scheduled task menjadi prompt yang tidak memakai path
  Windows.
- Buat `run.py` dan validasi output.
- Gunakan mode dry run agar pengembangan tidak selalu mengunggah ke Drive.

### Fase 2, integrasi Drive

- Buat service account Google.
- Beri akses folder tujuan kepada email service account.
- Simpan credential hanya sebagai secret.

### Fase 3, VPS

- Clone repository.
- Buat virtual environment dan pasang dependency.
- Tambahkan cron jam 00.00 zona Asia Jakarta.
- Simpan log dan kirim notifikasi jika exit code gagal.

### Fase 4, GitHub Actions opsional

- Tambahkan workflow test pada setiap push.
- Tambahkan `workflow_dispatch` untuk run manual.
- Pertimbangkan schedule hanya jika VPS tidak digunakan.

## Keputusan yang perlu dibuat

Sebelum menulis runner:

1. Provider model dan web search yang akan digunakan.
2. VPS atau GitHub Actions sebagai scheduler utama.
3. Apakah output harian perlu ikut di-commit ke Git.
4. Metode autentikasi Google Drive, service account direkomendasikan untuk VPS.

