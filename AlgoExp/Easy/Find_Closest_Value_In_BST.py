# Recursive
def findClosestValueInBst(tree, target):
	return work(tree, target, tree.value)

def work (tree, target, closest):
	# if at the end of the tree, return last closest value
	print(closest)
	if tree is None:
		return closest
	# check if the distance between the current closest and the target is more than the new node value
	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value
	# recurse through sub tree and return the closest value	
	if tree.value > target:
		return work(tree.left, target, closest) # make sure not to forget return with recursion
	elif tree.value < target:
		return work(tree.right, target, closest)
	else:
		return closest

