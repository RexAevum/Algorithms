# Time - O(n)
# Space - O(n)
def firstDuplicateValue(array):
    # Write your code here.
    if len(array) < 2:
		return -1
	seen = set()
	for nr in array:
		if nr in seen:
			return nr
		seen.add(nr)
	return -1

# Given solution #
# Time - O(n)
# Space - O(1)
def firstDuplicateValueGiven(array):
    # Write your code here.
    if len(array) < 2:
		return -1
	for nr in array:
		mapIdx = abs(nr) - 1
		# Check if value is negative for duplicate
		if array[mapIdx] < 0:
			return abs(nr)
		else:
			array[mapIdx] *= -1
	return -1