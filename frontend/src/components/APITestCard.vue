<script setup lang="ts">

import { ref } from 'vue'
import axios from 'axios'
import BlurCard from './BlurCard.vue';

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
  <BlurCard width="100%" height="fit-content">
    <button @click="apiCall" :disabled="loading">
      {{ method.toUpperCase() }} {{ url }}
    </button>

    <pre v-if="loading">Loading...</pre>
    <pre v-if="error">Error: {{ error }}</pre>
    <pre v-if="response">{{ response }}</pre>
  </BlurCard>
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

</style>

