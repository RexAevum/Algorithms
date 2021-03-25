# Time - O(n/2) => O(n)
# Space - O(1)
def isPalindrome(string):
	if len(string) < 2:
		return True
    # Set up 2 pointers for comparison
    left = 0
	right = len(string)-1
	
	# while the pointers have not met, compare
	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True

# Solution using recursion
def isPalindromeRec(string, i=0):
    # get the coresponding char from the other end
    j = len(string) - 1 - i
    return True if string[i] == string[j] and isPalindromeRec(string, i + 1)