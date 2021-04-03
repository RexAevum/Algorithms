# Time - O(n + d) where n is len of characters and d is len of document
# Space - O(c) where c is the number of unique char in characters
def generateDocument(characters, document):
    if len(characters) < len(document):
		return False
	
	chars = {}
	# check what chars are available
	for i in characters:
		if i not in chars:
			chars[i] = 1
		else:
			chars[i] += 1
			
	# check if we can make document 
	for i in document:
		if i not in chars:
			return False
		else:
			chars[i] -= 1
			if chars[i] < 0:
				return False
	return True

# Given Solution

# Time - O(n + d) where n is len of characters and d is len of document
# Space - O(c) where c is the number of unique char in characters
def generateDocumentGiven(characters, document):
    if len(characters) < len(document):
		return False
	
	chars = {}
	# check what chars are available
	for i in characters:
		if i not in chars:
			chars[i] = 0
		chars[i] += 1
			
	# check if we can make document 
	for i in document:
		if i not in chars or chars[i] == 0:
			return False
        chars[i] -= 1

    return True