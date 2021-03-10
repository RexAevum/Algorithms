# More optimal for time 
# Time - O(n)
# Space - O(n) --> since hash
def twoNumberSum(array, targetSum):
    # Write your code here.
	# For each element in the array travers the rest of the arrray and see if the the sums match the 
	# target sum
	ys = {} # store the past values from array
	out = []
	for i in array:
		y = targetSum - i
		if y in ys: # Looking if the needed difference is in the hash
			out.extend([i, y])
		else:
			ys[i] = True
	return out

# More optimal for space 
# Time - O(n^2)
# Space - O(1) --> no extra space was used
def twoNumberSum1(array, targetSum):
    # Write your code here.
    for i in range(len(array) - 1): # No point doing the last item
		# i is the index, since range is used
		x = array[i]
		for j in range(i + 1, len(array)):
			y = array[j]
			if x + y == targetSum:
				return [x, y]
	return []