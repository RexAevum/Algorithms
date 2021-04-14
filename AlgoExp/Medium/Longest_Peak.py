# Time - O(n)
# Space - O(1)
def longestPeak(array):
    # Write your code here.
    if len(array) < 3:
		return 0
	longest = 0
	i = 1
	while i < len(array) - 1:
		isPeak = array[i] > array[i-1] and array[i] > array[i+1]
		# check if current index is a peak
		if not isPeak:
			i += 1
			continue
		# if it is -> check the following items to count longest peak
		# we move pointer by 2 indexes to compare the current and the next value (left to right)
		left = i - 2 
		right = i + 2
		while left >= 0 and array[left] < array[left+1]:
			left -= 1
		while right < len(array) and array[right] < array[right-1]:
			right += 1
		# calc peak len
		peakLen = right - left - 1
		if peakLen > longest:
			longest = peakLen
		# since all valus left of the right index are part of the current peak can skip over them
		i = right
	return longest