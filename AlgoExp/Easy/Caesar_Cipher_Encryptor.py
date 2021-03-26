# Time - O(n)
# Space - O(n)
def caesarCipherEncryptor(string, key):
    # Write your code here.
	cipher = []
	key = key % 26
    for i in range(len(string)):
		val = ord(string[i])
		print(val)
		if val + key > 122:
				dif = (val + key) % 122
				val = 96 + dif
		else:
			val += key
		print("val after key: {} and char: {}".format(val, chr(val)))
		cipher.append(chr(val))
		
	return "".join(cipher)

# Given Solution
# Time - O(n)
# Space - O(n)
def caesarCipherEncryptorGiven(string, key):
    newString = []
    newKey = key % 26
    for letter in string:
        newString.append(getNewLetter(letter, newKey))
    return "".join(newString)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    # if new letter is out of the alphabet, wrap around
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + (newLetterCode % 122))