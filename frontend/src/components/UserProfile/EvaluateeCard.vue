<script setup lang="ts">
import BlurCard from '../BlurCard.vue'
import BlueCard from '../BlueCard.vue'
import Avatar from '../Avatar.vue'

const props = defineProps<{
	user: string
}>()
</script>

<template>
	<BlurCard
		id="evaluatee-profile"
		style="flex: 1; display: flex; flex-direction: column; padding: 1.5rem; gap: 1.5rem;">
	<h1 class="profile-card-title">
		Evaluatee profile
	</h1>
	<div id="evaluatee-profile-middle">
		<div id="evaluatee-metrics">
			<p>Total evaluations: 150</p>
			<p>Average time: 26min</p>
			<p>Average grade: 97</p>
			<p>Flagged evaluations: 7</p>
		</div>
		<BlueCard
			style="height: fit-content; flex: 1; display: flex; flex-direction: column; padding: 0.5rem;">
			<table>
				<thead>
					<tr>
						<th></th>
						<th>intra</th>
						<th>evaluations</th>
						<th>grade</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<th><Avatar src="/src/assets/default_avatar.jpg"/></th>
						<th>ljeribha</th>
						<th>17</th>
						<th>97%</th>
					</tr>
					<tr>
						<th><Avatar src="/src/assets/default_avatar.jpg"/></th>
						<th>gpochon</th>
						<th>13</th>
						<th>125%</th>
					</tr>
					<tr>
						<th><Avatar src="/src/assets/default_avatar.jpg"/></th>
						<th>ljaqcuem</th>
						<th>9</th>
						<th>83%</th>
					</tr>
				</tbody>
			</table>
		</BlueCard>
	</div>
	<div id="evaluatee-graph">

	</div>
	</BlurCard>
</template>

<style lang="css" scoped>
#evaluatee-profile-middle {
	display: flex;
	flex-direction: row;
	width: 100%;
	height: fit-content;
}

#evaluatee-metrics {
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

#evaluatee-graph {
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