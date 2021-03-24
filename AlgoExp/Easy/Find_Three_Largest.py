# Time - O(n)
# Space - O(1)
def findThreeLargestNumbers(array):
    # Write your code here.
    results = [None, None, None]
	for nr in array:
		findLargest(results, nr)
	return results

def findLargest(list, nr):
	if list[2] is None or list[2] < nr:
		shiftLargest(list, nr, 2)
	elif list[1] is None or list[1] < nr:
		shiftLargest(list, nr, 1)
	elif list[0] is None or list[0] < nr:
		shiftLargest(list, nr, 0)
		
def shiftLargest(list, nr, index):
	for i in range(index + 1): # +1 due to range being non-inclusive
		if i == index:
			list[i] = nr
		else:
			list[i] = list[i+1]