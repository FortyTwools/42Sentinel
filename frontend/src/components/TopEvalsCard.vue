<script lang="ts" setup>
import BlueCard from './BlueCard.vue';
import { TopRow } from './UserProfile/profile.types';
import Avatar from './Avatar.vue';

const props = defineProps<{
	data: TopRow[]
}>()
</script>

<template>
	<BlueCard
	style="height: fit-content; flex: 1; display: flex; flex-direction: column; padding: 0.5rem;">
		<table>
			<thead>
				<tr>
					<th />
					<th>intra</th>
					<th>evaluations</th>
					<th>grade</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="row in data">
					<th><Avatar src="/src/assets/default_avatar.jpg" /></th>
					<th>{{ row['login'] }}</th>
					<th>{{ row['count'] }}</th>
					<th>{{ (row['tot_mark'] / row['count']).toFixed(0) }}</th>
				</tr>
			</tbody>
		</table>
	</BlueCard>
</template>

<style lang="css" scoped>

thead {
	color: #95B0B0;
}

tbody > tr > th {
	color: #FFFFFF;
	font-weight: 450;
}

</style>