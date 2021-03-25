# Time - O(n^2)
# Space - O(1)
# Best: Time - O(n) | Space - O(1)
# AVG: Time - O(n^2) | Space - O(1)
# Best: Time - O(n^2) | Space - O(1)
def insertionSort(array):
    # Check if we need to sort array
    if len(array) < 2:
		return array
	# starting from the second item check if current is larger than the previos
	for i in range(1, len(array)):
		# incremented on in the while loop
		j = i
		# keep swapping the items until they are in order
		while j > 0 and array[j] < array[j-1]:
			swap(j, j-1, array)
			j -= 1
	return array

def swap(j, i, arr):
	arr[j], arr[i] = arr[i], arr[j]