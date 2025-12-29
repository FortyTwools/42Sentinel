<script setup lang="ts">
defineProps<{
	src: string
}>()

</script>

<template>
	<img :src="src" alt="Avatar"/>
</template>

<style lang="css" scoped>
img {
	width: 1.25rem;
	height: 1.25rem;
	border-radius: 100%;
}
</style>