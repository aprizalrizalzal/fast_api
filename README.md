# FastAPI dan Vue

*Back End* dengan FastAPI dan *Front End* dengan Vue.
- Setiap tabel menggunakan `id` unik
- **Tabel `users`**: field `name`, `birth_date`.
- **Tabel `user_images`**: field `image_url`, Menyimpan gambar yang di upload relasi ke `user_id`.

# Menjalankan Back End
```bach
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

# Menjalankan Front End
```bach
cd frontend
npm install
npm run dev
```

# Pengaturan Lingkungan
Port:
 - Back End: 8000
 - Front End: 3000

# Catatan
  - ```bash
    python --version
    Python 3.10.0
  - Pada frontend belum sepenuhnya menampilkan pesan kesalahan saat melakukan methode ke backend, lebih mengunakan (DevTools) bawaan browser
  - Saya tidak menggunakn Virtual Environment `.venv`
  - `requirements.txt` Mencantumkan semua paket yang terinstal di sistem yang saya pakai (Global).

