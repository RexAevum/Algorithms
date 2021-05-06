# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return helpBST(tree, float("-inf"), float("+inf"))

# Time - O(n)
# Space - O(d) where d is the depth of the tree due to recursion
def helpBST(node, min, max):
	if node is None:
		return True
	elif node.value < min or node.value >= max:
		return False
	# check left and right sub-trees
	leftSubValid = helpBST(node.left, min, node.value)
	rightSubValid = helpBST(node.right, node.value, max)
	return leftSubValid and rightSubValid