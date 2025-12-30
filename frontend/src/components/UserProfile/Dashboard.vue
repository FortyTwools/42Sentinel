<script setup lang="ts">
import BlurCard from '../BlurCard.vue'

const props = defineProps<{
	user: string
}>()
</script>

<template>
	<BlurCard
		id="sniping-dashboard"
		style="flex: 1">
	</BlurCard>
</template>