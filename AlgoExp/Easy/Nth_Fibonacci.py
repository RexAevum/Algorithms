# Time - O(2^n) --> every fib function will call 2 another 2 fib functions
# Space - O(n) --> because before all calls get placed on the call stack, they will be erased before getting more than n frames
def getNthFib(n):
    if n == 1:
		return 0
	elif n == 2:
		return 1
	return getNthFib(n-1) + getNthFib(n-2)

# Had to modify function call
# Time = O(n) --> pulling from hash is in constant time, so each fib number will only be calculated once 
# Space = O(n)
def getNthFib(n, memory={1 : 0, 2 : 1}):
    # Write your code here.
	if n in memory:
		return memory[n]
	else:
		memory[n] = getNthFib(n-1, memory) + getNthFib(n-2, memory)
		return memory[n]

# Time - O(n) | Space - O(n)
def getNthFib(n):
    # Write your code here.
    fib = [0, 1]
	i = 2
	while i <= n:
		nextNr = fib[i-1] + fib[i-2]
		fib.append(nextNr)
		i += 1
	return fib[n-1]

# Time - O(n) | Space - O(1)
def getNthFib(n):
    # Write your code here.
    last2 = [0, 1]
	i = 3 # first 2 are known
	while i <= n:
		nextFib = last2[0] + last2[1]
		last2[0] = last2[1]
		last2[1] = nextFib
		i += 1
	return last2[1] if n > 1 else last2[0]