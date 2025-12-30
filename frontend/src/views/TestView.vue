<script setup lang="ts">
import APITest from '../components/APITestCard.vue'
</script>

<template>
  <section>
    <APITest method="get" url="/api/v1/health"/>
    <APITest method="post" url="/api/v1/fetch/users" />
    <APITest method="get" url="/api/v1/db/ft_users" />
    <APITest method="get" url="/api/v1/db/projects" />
    <APITest method="get" url="/api/v1/processed/intra/valgrant" />
    <APITest method="dskjfbqs" url="test" />
  </section>
</template>

<style lang="css" scoped>

section {
  flex: 1;
  display: flex;
  padding: 2rem;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

</style>