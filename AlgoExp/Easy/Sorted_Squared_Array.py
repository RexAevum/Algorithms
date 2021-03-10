def sortedSquaredArray(array):
    # With two pointers - O(N)
    leftIdx = 0
	rightIdx = len(array) - 1
	squared = [0 for _ in array]
	#
	for i in reversed(range(len(array))):
		leftValue = array[leftIdx]
		rightValue = array[rightIdx]
		# compare abs
		if (abs(leftValue) >= abs(rightValue)):
			squared[i] = leftValue * leftValue
			leftIdx += 1
		else:
			squared[i] = rightValue * rightValue
			rightIdx -= 1
			
	return squared

def sortedSquaredArrayB(array):
    # Bruit force - O(n log n)
	out = [0 for _ in array] # create an array of 0s with the same length as array
    for i in range(len(array)):
		x = array[i]
		out[i] = x * x
		
	out.sort()
	return out