<script setup lang="ts">
import APITest from '../components/APITestCard.vue'
</script>

<template>
  <div>
    <section>
      <APITest method="get" url="/api/v1/health" />
      <APITest method="post" url="/api/v1/raw/fetch/users" />
      <APITest method="post" url="/api/v1/raw/fetch/users?campus=59" />
      <APITest method="dskjfbqs" url="test" />
    </section>
  </div>
</template>
