<script setup lang="ts">
import { useRoute } from 'vue-router'
import BlurCard from '../components/BlurCard.vue'
import BlueCard from '../components/BlueCard.vue'
import Avatar from '../components/Avatar.vue'

const route = useRoute()
const intra = route.params.intra
console.log(intra)
</script>

<template>
	<div class="page-container">
		<div class="lhs-container">
			<BlurCard
				id="user-profile"
				style="height: 100%; width: 100%; display:flex; flex-direction: column; align-items: center; padding: 2rem;">
			</BlurCard>
		</div>
		<div class="rhs-container">
			<div class="profiles-container">
				<BlurCard
					id="evaluator-profile"
					style="flex: 1; display: flex; flex-direction: column; padding: 1.5rem; gap: 1.5rem;">
				<h1 class="profile-card-title">
					Evaluator profile
				</h1>
				<div id="evaluator-profile-middle">
					<div id="evaluator-metrics">
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
				<div id="evaluator-graph">

				</div>
				</BlurCard>
				<BlurCard
					id="evaluatee-profile"
					style="flex: 1">
				</BlurCard>
			</div>
			<BlurCard
				id="sniping-dashboard"
				style="flex: 1">
			</BlurCard>
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

#evaluator-profile-middle, #evaluatee-profile-middle {
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