def isValidSubsequence(array, sequence):
    # Write your code here.
	pointerArray = 0
	pointerSequence = 0
	
	while pointerArray < len(array) and pointerSequence < len(sequence):
		if array[pointerArray] == sequence[pointerSequence]:
			pointerSequence += 1
		pointerArray += 1
	
	return pointerSequence == len(sequence)

    # Test

array= [5, 1, 2, 22, 25, 6, -1, 8, 10]
sequence= [1, 6, -1, 10]

print (isValidSubsequence(array, sequence));