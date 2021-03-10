def tournamentWinnerMy(competitions, results):
    # My solution 1
	teams = {}
    # O(n)
	for i in range(len(results)):
		
		if (results[i] == 1):
			won = competitions[i][0]
		else:
			won = competitions[i][1]
		# Create dict of scores
		if won in teams:
			teams[won] += 3
		else:
			teams[won] = 3
	# return max value key - O(n)
	return max(teams, key=teams.get)


# Given solution
WIN_NR = 1
WON_POINTS = 3

def tournamentWinner(competitions, results):
    # Write your code here.
    lead = ""
    # add lead to points dict for later comparison
	points = {lead : 0}
	
    # enumarate will help create an index for each item in list
	for index, competition in enumerate(competitions):
		currentResult = results[index]
		homeTeam, awayTeam = competition
		# get the winner
		winner = homeTeam if currentResult == WIN_NR else awayTeam
		# call helper method to update scores for the winning team
		updateScores (winner, WON_POINTS, points)
		
		if (points[winner] > points[lead]):
			lead = winner
			
	return lead

def updateScores(team, nrPoints, points):
	if team not in points:
		points[team] = 0
	points[team] += nrPoints