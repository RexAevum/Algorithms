# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time - O(n) --> since we must cover all nodes
# Space - O(n) --> it is O(n/2) since about half of the nodes in BST are leafs
def branchSums(root):
    # create sums list to be returned 
	sums = []
	# call method for df traversal
	getSumsDfs(root, 0, sums)
	return sums

def getSumsDfs(node, givenSum, sums):
	# if the current node is null, return --> since the given node does not exist
	if node is None:
		return
	# add new nodes value to the runningSum
	runningSum = node.value + givenSum
	# chekc if node is a leaf
	if node.left is None and node.right is None:
		# add to the sums list the sum value of the given branch
		sums.append(runningSum)
		# since it's a leaf, cannot call recursive for childern so return
		return
	# recursive call for dft
	getSumsDfs(node.left, runningSum, sums)
	getSumsDfs(node.right, runningSum, sums)