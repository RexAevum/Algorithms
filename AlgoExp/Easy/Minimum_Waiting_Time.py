def minimumWaitingTime(queries):
    # Sort list asc for optimal waittime
    queries.sort(reverse=False)
	waitTime = 0
	queryTime = 0
	# itterate through the queries add sum up the wait time
	for time in queries:
		waitTime += queryTime
		queryTime += time
	return waitTime