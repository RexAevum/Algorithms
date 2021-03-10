# v > c + 1 --> cannot create c + 1
# where v - coin | c - change  
def nonConstructibleChange(coins):
    # first sort the array
	coins.sort()
    change = 0 # for sum of coins
	
    # for each coin check if it's larger than the cumulative sum of change + 1
    # if it greater, that means we cannot create change + 1
    # if less or equal --> can create all subsets of the superset number
	for coin in coins:
		if change + 1 < coin:
			return change + 1
		else:
			change += coin
	return change + 1 # we start with change = 0