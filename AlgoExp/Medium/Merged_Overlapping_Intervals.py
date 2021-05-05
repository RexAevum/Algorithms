# Time - O(nlog n )
# Space - O(n)
def mergeOverlappingIntervals(intervals):
    # Write your code here.
	if len(intervals) < 2:
		return intervals
	sortedInt = sorted(intervals, key=lambda x: x[0])
	# create a new merged list
	mergedInt = []
	# get reference to first item in sorted list
	currentInt = sortedInt[0] # reference
	# add it to the merged list
	mergedInt.append(currentInt)
	# travers the rest of the merged list and check for overlap
	for nextInt in sortedInt:
		_, currentEnd = currentInt
		nextStart, nextEnd = nextInt
		# if there is overlap, just take the largest of the 2 intevals second nr
		if currentEnd >= nextStart:
			# since we have it by reference, updating this is gonna update the currentInt in the mergedInt
			currentInt[1] = max(currentEnd, nextEnd)
		else:
			# if there is no overlap, update reference and add it to the new list
			currentInt = nextInt
			mergedInt.append(currentInt)
	return mergedInt