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

    async fetchUsers() {
      const response = await api.get('/users')

      this.users = response.data.users

      return response.data.users
    },

    async fetchUserById(userIds) {
      const response = await api.get('/users')

      this.user = response.data

      return response.data
    },

    async deleteUserById(userIds) {
      const response = await api.delete('/users')

      this.message = response.data.message

      await this.fetchUsers()

      return response.data
    },
  },
})
