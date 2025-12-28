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
  <div class="api-card">
    <button @click="apiCall" :disabled="loading">
      {{ method.toUpperCase() }} {{ url }}
    </button>

    <pre v-if="loading">Loading...</pre>
    <pre v-if="error">Error: {{ error }}</pre>
    <pre v-if="response">{{ response }}</pre>
  </div>
</template>

<style scoped>

button {
  color: #fff;
  font-weight: 700;
  width: fit-content;
  padding: 1rem;
  border-radius: 1rem;
  background-color: #04809F;
  border: none;
}

p, pre {
  padding: 1rem;
  border-radius: 1rem;
  background-color: #ffffff4f;
}
/* Container */

.api-card {
  width: 100%;

  display: flex;
  flex-direction: column;
  padding: 10px;
  gap: 10px;

  position: relative;

  background: radial-gradient(90.16% 143.01% at 15.32% 21.04%, rgba(255, 255, 255, 0.2) 0%, rgba(4, 128, 159, 0.04) 37.98%, rgba(237, 52, 145, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */;
  background-blend-mode: overlay, normal;
  border: 2px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(40px);
  border-radius: 20px;
}

</style>

