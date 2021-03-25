# Time - O(n^2)
# Space - O(1)
# Best: Time - O(n^2) | Space - O(1)
# AVG: Time - O(n^2) | Space - O(1)
# Best: Time - O(n^2) | Space - O(1)
def selectionSort(array):
    # Write your code here.
    if len(array) < 2:
		return array
	idx = 0
	while idx < len(array) - 1:
		smallestIdx = idx
		for i in range(idx, len(array)):
			if array[i] < array[smallestIdx]:
				smallestIdx = i
		swap (idx, smallestIdx, array)
		idx += 1
	return array

def swap (idx, sm, a):
	a[idx], a[sm] = a[sm], a[idx]