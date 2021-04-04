# Time - O(n)
# Space - O(1)
def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
	j = len(array) - 1
	while i < j:
		# swap the toMove value and the other value
		if array[i] == toMove and array[j] != toMove:
			array[i], array[j] = array[j], array[i]
			i += 1
			j -= 1
		# move left pointer if it has not found toMove value
		elif array[i] != toMove:
			i += 1
		# move right if it HAS found the toMove value
		elif array[j] == toMove:
			j -= 1
	return array