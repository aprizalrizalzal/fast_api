import axios from 'axios'

// Buat instance axios dengan konfigurasi default
const api = axios.create({
  baseURL: 'http://localhost:8000', // URL API backend
  timeout: 5000, // Batas waktu untuk setiap permintaan
  withCredentials: true, // Mengirim cookie dengan setiap permintaan
  withXSRFToken: true,
  headers: {
    Accept: 'application/json', // Pastikan permintaan mengharapkan JSON
  },
})

export default api
