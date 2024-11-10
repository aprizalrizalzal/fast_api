<script setup>
import { onMounted, ref } from 'vue'
import { useStore } from './stores/stores'

const users = ref([])
const user = ref({
  id: '',
  name: '',
  birth_date: ''
})

const message = ref('')

const store = useStore()

const fetchWelcome = async () => {
  message.value = await store.fetchWelcome()
}

const fetchUsers = async () => {
  users.value = await store.fetchUsers()
}

onMounted(() => {
  fetchWelcome()
  fetchUsers()
})

function saveUser() {
  store.postUsers(user.value).then((data)=> {
    if (data) {
      fetchUsers()
    }
  })
}

function getUserById(userId) {
  store.fetchUserById(userId).then((data) => {
    if (data) {
      user.value = data
      user.value.id = data.id
    }
  })
}

const handleImageFileUpload = async (event) => {
  const selectedFile = event.target.files[0];

  if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      store.postImageByUserId(user.value.id, formData)
  }
};

function deletUserById(userId) {
  store.deleteUserById(userId).then((data) => {
    if (data) {
      fetchUsers()
    }
  })
}
</script>

<template>
  <header>
    <div class="container">
      <div class="my-4">
        <h1>{{ message }}</h1>
        <h2>Vite + Vue</h2>
      </div>
    </div>
  </header>

  <main class="container">
    <div>
      <div class="my-4">
        <form @submit.prevent="saveUser()">
          <div class="form-group">
            <label for="name">Nama</label>
            <input type="text" class="form-control" id="name" v-model="user.name" required>
          </div>
          <div class="form-group">
            <label for="birth_date">Tanggal Lahir</label>
            <input type="date" class="form-control" id="birth_date" v-model="user.birth_date" required>
          </div>
          <button type="submit" class="btn btn-primary">Simpan</button>
        </form>
      </div>  
      <div class="my-4">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Nama</th>
              <th scope="col">Tanggal Lahir</th>
              <th scope="col">Umur</th>
              <th scope="col">Ulang Tahun</th>
              <th scope="col">Aksi</th>
            </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="user.id">
            <td>
              {{ index + 1 }}
            </td>
            <td>
              {{ user.name }}
            </td>
            <td>
              {{ user.birth_date }}
            </td>
            <td>
              {{ user.age }} Tahun
            </td>
            <td>
              Dalam <b>{{ user.months_to_bday }}</b> Bulan atau <b>{{ user.days_to_bday }}</b> Hari lagi
            </td>
            <td>
              <div class="d-flex flex-nowrap">
                <button type="button" class="btn btn-primary mx-2" @click="getUserById(user.id)">Detail</button>
                <button type="button" class="btn btn-danger mx-2" @click="deletUserById(user.id)">Hapus</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      </div>
    </div>
    <div v-if="user.id" class="my-4">
      <div class="card" style="width: 18rem;">
        <img v-if="user.images[0]?.image_url" :src="`http://localhost:8000/${user.images[0]?.image_url}`" class="card-img-top" :alt="user.name">
        <div v-else class="mt-3 mx-3">
          <input type="file" @change="handleImageFileUpload" class="form-control" id="upload" style="display: none" />
          <label class="btn btn-primary shadow-sm me-2" for="upload"><i class="bi bi-upload"></i>Upload Gambar</label>
        </div>
        <div class="card-body">
          <p class="card-text">Saat ini berusia <b>{{ user.age }} tahun</b>, dan dalam waktu <b>{{ user.months_to_bday }} bulan</b> atau sekitar <b>{{ user.days_to_bday }} hari</b>, akan mencapai usia <b>{{ user.age + 1 }} tahun</b>.</p>
        </div>
        <div v-for="image in user.images" :key="image.id">
          <img v-if="user.images.length > 1" :src="`http://localhost:8000/${image.image_url}`" class="card-img-top" :alt="user.name">
          <button type="button" class="btn btn-danger mx-2" @click="deletUserImageById(image.id)">Hapus</button>
        </div>
      </div>
    </div>
  </main>
</template>