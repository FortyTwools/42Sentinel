<script setup lang="ts">

import axios from 'axios'
import { ref, onMounted } from 'vue'
import BlurCard from '../BlurCard.vue'
import Spinner from '../Spinner.vue'
import TopEvalsCard from '../TopEvalsCard.vue'
import { Evaluatee, HTTPError } from './profile.types'
import SpinnerWrapper from '../SpinnerWrapper.vue'
import HTTPErrorCard from '../HTTPErrorCard.vue'

const props = defineProps<{
	user: string
}>()

const pageState = ref("loading")
const data = ref<Evaluatee | null>(null)
const error = ref<HTTPError | null>(null)

onMounted(async () => {
	let response:any
	try {
		response = await axios.get(`/api/v1/evaluated/${props.user}`)
		if (response['status'] !== 200)
			throw Error()
		data.value = response['data']['data']
		pageState.value = "fetched"
	} catch (err: any) {
		console.log("DEBUGDEBUGDEBUG:", err)
		error.value = {"code": err['status'], "message": err.response?.statusText, "reason": err.response?.data?.detail}
		pageState.value = "error"
	}
})

function isLoading(): boolean {
	return pageState.value === "loading"
}

</script>

<template>
	<BlurCard
		id="evaluated-profile"
		style="flex: 1; display: flex; padding: 1.5rem;"
	>

		<SpinnerWrapper v-if="isLoading()">
			<Spinner />
		</SpinnerWrapper>
		<div v-else-if="data" id="evaluated-container">
			<div id="evaluated-title">
				<h1 class="profile-card-title">
					Evaluated profile
				</h1>
			</div>
			<div id="evaluated-profile-middle">
				<div id="evaluated-metrics">
					<p>Total evaluations: {{ data['total'] }}</p>
					<p>Average time: {{ data['avg_time'] }}min</p>
					<p>Average grade: {{ data['avg_grade'].toFixed(2) }}</p>
					<p>Ev. per project: 4.2</p>
				</div>
				<TopEvalsCard :data="data['top']"/>
			</div>
			<div id="evaluated-graph">
			</div>
		</div>
		<HTTPErrorCard v-else-if="error" :error="error" />
	</BlurCard>
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

#evaluated-container {
	flex: 1; 
	display: flex;
	flex-direction: column;
	gap: 1.5rem;
}

#evaluated-title {
	width: 100%;
	height: fit-content;
}

#evaluated-profile-middle {
	display: flex;
	flex-direction: row;
	width: 100%;
	height: fit-content;
}

#evaluated-metrics {
	display: flex;
	flex-direction: column;
	gap: .25rem;
	flex: 1;
	font-size: 1.25em;
	color: white;
}

.profile-card-title {
	color: white;
	font-weight: bold;
}

#evaluated-graph {
	flex: 1;
	background-color: #12141A;
	border-radius: 15px;
}

</style>