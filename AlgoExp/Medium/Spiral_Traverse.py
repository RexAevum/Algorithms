# Time - O(n)
# Space - O(n)
def spiralTraverse(array):
    # Write your code here.
    startRow = 0
	endRow = len(array) - 1
	startCol = 0
	endCol = len(array[0]) - 1
	results = []
	# 
	while startRow <= endRow and startCol <= endCol:
		# Go left -> itterate col
		for col in range(startCol, endCol+1):
			results.append(array[startCol][col])
		# Go down -> itterate row
		for row in range(startRow + 1, endRow + 1):
			results.append(array[row][endCol])
		# Go left -> reverse and itterate through col
		for col in reversed(range(startCol, endCol)): # endCol so we dont count the same num twice
			if startRow == endRow:
				break
			results.append(array[endRow][col])
		# Go up -> itterate row in reverse
		for row in reversed(range(startRow + 1, endRow)):
			if startCol == endCol:
				break
			results.append(array[row][startCol])
		# jump to the next layer/perimiter
		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1
	return results