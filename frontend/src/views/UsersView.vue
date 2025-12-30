<script setup lang="ts">
import { useRoute } from 'vue-router'

import Dashboard from '../components/UserProfile/Dashboard.vue'
import EvaluateeCard from '../components/UserProfile/EvaluateeCard.vue'
import EvaluatorCard from '../components/UserProfile/EvaluatorCard.vue'
import ProfileCard from '../components/UserProfile/ProfileCard.vue'


const route = useRoute()
const user: string = Array.isArray(route.params.user)
  ? route.params.user[0]
  : route.params.user
</script>

<template>
	<div class="page-container">
		<div class="lhs-container">
			<ProfileCard :user="user"/>
		</div>
		<div class="rhs-container">
			<div class="profiles-container">
				<EvaluatorCard :user="user"/>
				<EvaluateeCard :user="user"/>
			</div>
			<Dashboard :user="user" />
		</div>
	</div>
</template>

<style lang="css" scoped>

.page-container {
	display: flex;
	flex-direction: row;
	flex: 1;
	padding: 4rem;
}

.lhs-container {
	width: 30%;
	height: 100%;
}

.rhs-container {
	display: flex;
	flex-direction: column;
	flex: 1;
	padding-left: 4rem;
	gap: 4rem;
}

.profiles-container {
	width: 100%;
	height: 45%;
	display: flex;
	flex-direction: row;
	gap: 4rem;
}

</style>