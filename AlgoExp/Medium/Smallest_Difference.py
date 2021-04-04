# Time - O(n * m) where n is len(arrayOne) and m is len(arrayTwo)
# Space - O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    smallest = [arrayOne[0], arrayTwo[0]]
	for i in range(len(arrayOne)):
		for j in range(len(arrayTwo)):
			if abs(smallest[0] - smallest[1]) > abs(arrayOne[i] - arrayTwo[j]):
				smallest = [arrayOne[i], arrayTwo[j]]
	return smallest

# Time - O(n log(n) + m log(m))
# Space - O(1)
def smallestDifferenceGiven(arrayOne, arrayTwo):
    # Write your code here.
    # sort both arrays
	arrayOne.sort()
	arrayTwo.sort()
	# set up pointers
	p1 = 0
	p2 = 0
	# track smallest diff and pair
	smallestPair = []
	smallest = float("inf")
	# keep itterating till all numbers are covered
	while p1 < len(arrayOne) and p2 < len(arrayTwo):
		first = arrayOne[p1]
		second = arrayTwo[p2]
		currentDiff = abs(first - second)
		# check which pointer to increment
		if first > second:
			p2 += 1
		elif first < second:
			p1 += 1
		else:
			return [first, second]
		# check if current pair itteration is less than the previos ones
		if smallest > currentDiff:
			smallest = currentDiff
			smallestPair = [first, second]
	return smallestPair