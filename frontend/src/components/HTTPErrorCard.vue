<script setup lang="ts">
import { HTTPError } from './UserProfile/profile.types'

const props = defineProps<{
	error: HTTPError
}>()

</script>

<template>
	<div class="container">
		<h1>{{ props.error.code }} {{ props.error?.message }}</h1>
		<h2>{{ props.error?.reason }}</h2>
	</div>
</template>

<style lang="css" scoped>

.container {
	flex: 1;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	color:#FFF;
}

</style>