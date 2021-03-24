# Best: Time - O(n) | Space - O(1)
# Avg: Time - O(n^2) | Space - O(1)
# Worst: Time - O(n^2) | Space - O(1)
def bubbleSort(array):
    if len(array) < 2:
		return array
    isSorted = False
	# counter is used to 
	counter = 0
	# check if sorted -> if any changes were made, we need to check again
	while not isSorted:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i+1] is not None and array[i] > array[i+1]:
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
				isSorted = False
		counter += 1
	return array