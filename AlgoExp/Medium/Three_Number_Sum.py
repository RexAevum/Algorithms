# Time - O(n^2)
# Space - O(n) where n is len of array
def threeNumberSum(array, targetSum):
    if len(array) < 3:
		return []
	# sort array
	array.sort()
	# prep pointers and container
	sums = []
	# check if there are 3 values that sum to targetSum
	# itterate through array and set each number to current, left to i+1 and right to len(array) - 1
	for i in range(len(array)):
		current = array[i]
		left = i + 1
		right = len(array) - 1
		# use pointers to check if there is any combination that get's the targetSum
		while left < right:
			leftVal = array[left]
			rightVal = array[right]
			# if threeNumberSum is more than target, we need to shift the RIGHT pointer --> will reduce overall sum
			if current + leftVal + rightVal > targetSum:
				right -= 1
			# if threeNumberSum is more than target, we need to shift the LEFT pointer --> will reduce overall sum
			elif current + leftVal + rightVal < targetSum:
				left += 1
			# if we found targetSum, append to the sums array and move one of the pointers
			else:
				sums.append([current, leftVal, rightVal])
				left += 1 # doesn't matter which pointer is moved or both
	return sums