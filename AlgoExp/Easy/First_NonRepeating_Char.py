# Time - O(n)
# Space - O(26) since there are only 26 char in lowercase alphabet 
def firstNonRepeatingCharacter(string):
	check = {}
	for char in string:
		if char in check:
			check[char] += 1
		else:
			check[char] = 1
	for key, val in check.items():
		if val == 1:
			return string.index(key)
	return -1