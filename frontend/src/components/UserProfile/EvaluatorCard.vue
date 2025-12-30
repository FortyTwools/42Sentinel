<script setup lang="ts">

import axios from 'axios'
import { ref, onMounted } from 'vue'
import BlurCard from '../BlurCard.vue'
import Spinner from '../Spinner.vue'
import TopEvalsCard from '../TopEvalsCard.vue'

const props = defineProps<{
	user: string
}>()

const pageState = ref("loading")
const data = ref<any>(null)

onMounted(async () => {
	try {
		const response:any = await axios.get(`/api/v1/processed/intra/${props.user}`)
		console.log(response)
		if (response['status'] !== 200)
			throw Error(`${response['status']}: ${response['statusText']}`)
		data.value = response['data']
		pageState.value = "fetched"
	} catch (err: any) {
		console.error(err)
	}
})

function isLoading(): boolean {
	return pageState.value === "loading"
}

function isFetched(): boolean {
	return pageState.value === "fetched"
}

</script>

<template>
	<BlurCard
		id="evaluator-profile"
		style="flex: 1; display: flex; padding: 1.5rem;"
	>
		<div v-if="isLoading()" style="flex:1; display: flex; align-items: center; justify-content: center;">
			<Spinner />
		</div>
		<div v-else-if="isFetched()" id="evaluator-container">
			<div id="evaluator-title">
				<h1 class="profile-card-title">
					Evaluator profile
				</h1>
			</div>
			<div id="evaluator-profile-middle">
				<div id="evaluator-metrics">
					<p>Total evaluations: 150</p>
					<p>Average time: 26min</p>
					<p>Average grade: 97</p>
					<p>Flagged evaluations: 7</p>
				</div>
				<TopEvalsCard />
			</div>
			<div id="evaluator-graph">
			</div>
		</div>
		<div v-else>
			:c
		</div>
	</BlurCard>
</template>

<style lang="css" scoped>

#evaluator-container {
	flex: 1; 
	display: flex;
	flex-direction: column;
	gap: 1.5rem;
}

#evaluator-title {
	width: 100%;
	height: fit-content;
}

#evaluator-profile-middle {
	display: flex;
	flex-direction: row;
	width: 100%;
	height: fit-content;
}

#evaluator-metrics {
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

#evaluator-graph {
	flex: 1;
	background-color: #12141A;
	border-radius: 15px;
}

thead {
	color: #95B0B0;
}

tbody > tr > th {
	color: #FFFFFF;
	font-weight: 450;
}

</style>