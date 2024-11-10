import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import api from '@/service/api'
import { createPinia } from 'pinia'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)

app.config.globalProperties.$api = api

app.mount('#app')
