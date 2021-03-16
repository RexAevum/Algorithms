# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# Time - O(n)
# Space - o(d) where d is the greatest depth
def productSum(array, depth=1):
    # Check if None
    if array is None:
		return 0
	else:
		currentSum = 0
		for item in array:
			if type(item) == int:
				currentSum += item
			else:
				currentSum += productSum(item, depth + 1)
        # 
		return currentSum * depth