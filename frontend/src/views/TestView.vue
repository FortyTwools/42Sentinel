<script setup lang="ts">
import APITest from '../components/APITestCard.vue'
</script>

<template>
  <section>
    <APITest method="get" url="/api/v1/health" />
    <APITest method="post" url="/api/v1/raw/fetch/users" />
    <APITest method="get" url="/api/v1/raw/fetch/users" />
    <APITest method="dskjfbqs" url="test" />
  </section>
</template>

<style lang="css" scoped>

section {
  display: flex;
  margin: 2rem;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

</style>