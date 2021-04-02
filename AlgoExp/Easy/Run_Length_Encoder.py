# Time - O(n)
# Space - O(n)
def runLengthEncoding(string):
	# if a string is only once char, can return right away
    if len(string) < 2:
		return "1{}".format(string[0])
    encoded = [] # store the new string
	current = string[0] 
	count = 1
	for i in range(1, len(string)):
		if current == string[i]:
			count += 1
			# if str consists of the same char, have to encode
			if i == len(string) - 1:
				encodeToString(encoded, current, count)
		else:
			encodeToString(encoded, current, count)
			current = string[i]
			count = 1
			# if it's the last char the it have to call the encoder
			if i == len(string) - 1:
				encodeToString(encoded, current, count)
	return "".join(encoded)

def encodeToString(str, char, count):
	if count >= 10:
		count -= 9
		str.append("9{}".format(char))
		return encodeToString(str, char, count)
	else:
		str.append("{}{}".format(count, char))
		return

# Given solution
def runLengthEncodingGiven(string):
    # Write your code here.
    encoded = []
	currLen = 1
	
	for i in range(1, len(string)):
		currentChar = string[i]
		prevChar = string[i-1]
		
		# check if the same
		if currentChar != prevChar or currLen == 9:
			encoded.append(str(currLen))
			encoded.append(prevChar)
			currLen = 0
		# increment currLen if both char are the same
		currLen += 1
	# handle the last char
	encoded.append(str(currLen))
	encoded.append(string[len(string)-1])
	return "".join(encoded)