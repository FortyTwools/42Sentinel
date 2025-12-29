<script setup lang="ts">
</script>


<template>
	<div
		v-bind="$attrs"
		class="blur-card"
	>
	    <slot></slot>
	</div>
</template>

<style lang="css" scoped>
.blur-card {
	background: rgba(4, 128, 159, 0.3);
	border: 1px solid rgba(255, 255, 255, 0.2);
	border-radius: 15px;
}
</style>
