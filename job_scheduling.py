def job_scheduling(jobs):
	jobs.sort(key = lambda x :x[2] ,reverse=True)
	
	n = max(job[1] for job in jobs)
	slots = [None]*n
	total_profit = 0
	results = []
	
	for job in jobs:
		for i in range(job[1]-1,-1,-1):
			if slots[i] is None:
				slots[i] = job[0]
				total_profit+=job[2]
				results.append(job[0])
				break
	print("Total profit :",total_profit)
	print("Job Scheduls :" , results)
	
jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
job_scheduling(jobs)