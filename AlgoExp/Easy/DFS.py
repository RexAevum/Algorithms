class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	# Time - O(v + e) | Space - O(v)
    def depthFirstSearch(self, array):
        # Write your code here.
		array.append(self.name)
		if len(self.children) > 0: # Not needed since for loop will not itterate through an empty list
			for node in self.children:
				node.depthFirstSearch(array)
		return array