# Time - O(n)
# Space - O(1)
def isMonotonic(array):
    # Write your code here.
    if len(array) < 2:
		return True
	# check if items are increasing or decreasing in value
	# in case where all the elements are the same we can return true
	change = 0
	i = 0
	while change == 0 and i < len(array)-1:
		if array[i] > array[i+1]:
			change = -1
		elif array[i] < array[i+1]:
			change = 1
		i += 1
	# if all the elements were the same -> return true
	if change == 0:
		return True
	# check if the array is eithe increasing or decreasing consistently
	for i in range(1, len(array)):
		if array[i] > array[i-1] and change == -1:
			return False
		if array[i] < array[i-1] and change == 1:
			return False
	return True

# Time - O(n)
# Space - O(1)
def isMonotonicGiven(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range (1, len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing = False
        if array[i] < array[i-1]:
            isNonDecreasing = False
    #
    return isNonDecreasing or isNonIncreasing