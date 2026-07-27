# Brainstorming Deployment GitHub dan VPS

## Kondisi sekarang

Repository sudah memiliki `run.py` dan GitHub Actions manual. Runner memakai
Claude API dengan web search, membuat brief dan script, memvalidasi jumlah
output, lalu menyediakan hasil sebagai artifact GitHub.

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

Environment yang dibutuhkan saat ini:

```text
ANTHROPIC_API_KEY
CLAUDE_MODEL, opsional
```

Jangan commit file `.env` atau credential apa pun.

## Pilihan scheduler

### VPS cron, direkomendasikan

Kelebihan:

- Zona waktu dan jadwal lebih mudah dikontrol.
- File output dapat disimpan persisten.
- Lebih cocok untuk proses riset yang durasinya tidak selalu sama.

Kekurangan:

- Server perlu dipelihara.
- Log rotation dan alert kegagalan perlu disiapkan.

### GitHub Actions, aktif

Kelebihan:

- Tidak perlu mengelola server.
- Riwayat run dan log tersedia di GitHub.

Kekurangan:

- Secret Google dan API harus disimpan di GitHub Secrets.
- Output lokal hilang setelah job selesai kecuali diunggah atau di-commit.
- Schedule bukan pilihan ideal bila waktu eksekusi harus sangat presisi.

## Tahapan implementasi

### Fase 1, runner GitHub, selesai

- Runner dipicu manual.
- Push dan pull request hanya menjalankan self-check tanpa API.
- Output menjadi artifact dan tidak mengubah repository.

### Fase 2, verifikasi

- Tambahkan secret API di GitHub.
- Jalankan workflow manual.
- Periksa akurasi sumber, struktur output, biaya, dan durasi.

### Fase 3, integrasi Drive

- Tentukan autentikasi Google yang cocok dengan jenis folder tujuan.
- Simpan credential hanya sebagai secret.
- Aktifkan upload setelah artifact GitHub dinyatakan aman.

### Fase 4, VPS

- Clone repository.
- Buat virtual environment dan pasang dependency.
- Tambahkan cron jam 00.00 zona Asia Jakarta.
- Simpan log dan kirim notifikasi jika exit code gagal.

Schedule GitHub sengaja belum diaktifkan. Aktifkan hanya setelah beberapa run
manual konsisten dan batas biaya sudah disepakati.
