import api from '@/service/api' // Import instance Axios dari api.js
import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => ({
    users: [],
    user: null,
    message: null,
  }),

  getters: {
    getUsers() {
      return this.users
    },
    getUser() {
      return this.user
    },
  },

  actions: {
    async fetchWelcome() {
      const response = await api.get('/')

      this.message = response.data.message

      return response.data.message
    },

    async postUsers(userData) {
      const response = await api.post('/users', userData)

      this.user = response.data

      return response.data
    },

    async fetchUsers() {
      const response = await api.get('/users')

      this.users = response.data

      return response.data
    },

    async fetchUserById(userId) {
      const response = await api.get(`/users/${userId}`)

      this.user = response.data

      return response.data
    },

    async updateUserById(userId, userData) {
      const response = await api.put(`/users/${userId}`, userData)

      this.user = response.data

      return response.data
    },

    async postImageByUserId(userId, imageUser) {
      const headers = {
        'Content-Type': 'multipart/form-data',
      };

      const response = await api.post(`/user_images/?user_id=${userId}`, imageUser, {
        headers,
      });

      this.user = response.data

      return response.data
    },

    async deletUserImageById(imageId) {
      const response = await api.delete(`/user_images/${imageId}`)

      this.message = response.data.message

      await this.fetchUsers()

      return response.data
    },

    async deleteUserById(userId) {
      const response = await api.delete(`/users/${userId}`)

      this.message = response.data.message

      await this.fetchUsers()

      return response.data
    },
  },
})
