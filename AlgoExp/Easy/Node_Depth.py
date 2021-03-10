# Recursive 
# Avg Time - O(n)
# Avg Space - O(n)
def nodeDepthsRec(root):
    # Write your code here.
    depth = 0
	return getDepthSum(root, depth)
	

def getDepthSum(node, d):
	# if node doesnt exist, return 0 since it does not have a depth
	if node is None:
		return 0
	# add the current depth
	return d + getDepthSum(node.left, d + 1) + getDepthSum(node.right, d + 1)

