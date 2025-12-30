<script setup lang="ts">
import BlurCard from '../BlurCard.vue'

const props = defineProps<{
	user: string
}>()
</script>

<template>
	<BlurCard
		id="user-profile"
		style="height: 100%; width: 100%; display:flex; flex-direction: column; align-items: center; padding: 2rem;">
	</BlurCard>
</template>