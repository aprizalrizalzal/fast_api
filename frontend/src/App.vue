<script setup>
import { onMounted, ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import { useStore } from './stores/stores';

const store = useStore();

const fetchWelcome = async () => {
  message.value = await store.fetchWelcome();
};

const fetchUsers = async () => {
    users.value = await store.fetchUsers();
};

onMounted(() => {
  fetchWelcome();
    fetchUsers();
});

const users = ref([]);
const user = ref({});
const message = ref({});

</script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld :msg="message" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
