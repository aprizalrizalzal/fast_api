# FastAPI dan Vue

*Back End* dengan FastAPI dan *Front End* dengan Vue.
- **Tabel `users`**: field `name`, `birth_date`, dan `id` unik.
- **Tabel `user_images`**: Menyimpan gambar yang di upload relasi ke `user_id`.

- Tidak menggunakn Virtual Environment `.venv`
- `requirements.txt` Mencantumkan semua paket yang terinstal di sistem.

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
  - Pada frontend belum sepenuhnya menampilkan pesan kesalahan saat melakukan methode ke backend, lebih mengunakan (DevTools) bawaan browser
