# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time - O(n) | Space - O(1)
def removeDuplicatesFromLinkedList(linkedList):
    # Grap first node of list
	current = linkedList
	while current is not None:
		nextNode = current.next
		# Jump over the nodes with the same value as current
		# Use while instead of if since can be more than 1 number in a row
		while nextNode is not None and current.value == nextNode.value: # check for none first, otherwise get an error
			nextNode = nextNode.next
		# reconnect list	
		current.next = nextNode
		# move pointer
		current = nextNode
	return linkedList