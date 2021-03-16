# Time - O(log n)
# Space - O(1)
def binarySearch(array, target):
    # Set up pointers for both ends of the list
	left = 0
	right = len(array) - 1
	while right >= left:
		mid = (left + right) // 2 # the '//' symbol will round down
		if (target == array[mid]):
			return mid
		# because we already check the array[mid], need to skip over the mid index by 1
		elif target > array[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return -1