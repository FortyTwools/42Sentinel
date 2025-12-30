export type TopRow = {
	"login": string,
	"tot_mark": number,
	"count": number,
}

export type Evaluatee = {
	avg_grade: number
	avg_time: number
	total: number
	top: TopRow[]
}

export type HTTPError = {
	code: number
	message: string
	reason?: string
}
