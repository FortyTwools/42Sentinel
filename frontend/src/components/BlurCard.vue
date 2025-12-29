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
	background: radial-gradient(90.16% 143.01% at 15.32% 21.04%, rgba(255, 255, 255, 0.2) 0%, rgba(4, 128, 159, 0.04) 37.98%, rgba(237, 52, 145, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */;
	background-blend-mode: overlay, normal;
	border: 2px solid rgba(255, 255, 255, 0.2);
	backdrop-filter: blur(40px);
	border-radius: 20px;
}
</style>
