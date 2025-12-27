<script setup lang="ts">

import { ref } from 'vue'
import axios from 'axios'

const props = defineProps<{
  method: string
  url: string
}>()

const response = ref<any>(null)
const error = ref<string | null>(null)
const loading = ref(false)

async function apiCall() {
  let axiosMethod;
  loading.value = true;
  error.value = null;
  
  try {
    switch (props.method) {
      default:
        throw new Error("wtf is this method");
      case 'get':
        axiosMethod = axios.get; break;
      case 'post':
        axiosMethod = axios.post; break;
    }
    const res = await axiosMethod(props.url);
    response.value = res.data
  } catch (err: any) {
    error.value = err.message ?? 'Request failed'
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <div>
    <section>
      <button @click="apiCall" :disabled="loading">{{method.toUpperCase()}} {{url}}</button>
      <p v-if="loading">Loading...</p>
      <p v-if="error">Error: {{ error }}</p>
      <pre v-if="response">{{ response }}</pre>
    </section>

  </div>
</template>

<style scoped>

div {
  width: 50%;
  padding: 1rem;
  overflow: auto;
  display: flex;
  flex-direction: column;  
}

section {
  display: flex;
  flex-direction: column;  
  gap: 1rem;
}

button {
  width: fit-content;
  padding: 1rem;
  border-radius: 1rem;
  background-color: #04809F;
  border: none;
}

p, pre {
  border-radius: 1rem;
  background-color: #ffffff4f;
}

</style>