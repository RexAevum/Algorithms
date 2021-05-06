class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	# insert node into a tree
	# Time - O(n) | Avg - O(log n)
	# Space - O(n) | Avg - O(log n)
    def insert(self, value):
		if self.value > value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
        return self
	# check if value in tree
	# Time - O(n) | Avg - O(log n)
	# Space - O(n) | Avg - O(log n)
    def contains(self, value):
        # Write your code here.
        if self.value == value:
			return True
		elif self.value > value:
			if self.left is not None:
				return self.left.contains(value)
			else:
				return False
		else:
			if self.right is not None:
				return self.right.contains(value)
			else:
				return False
		return False
	
	# Remove value from tree and rearange tree into BST
	# Time - O(n) | Avg - O(log n)
	# Space - O(n) | Avg - O(log n)
    def remove(self, value, p=None):
		if value < self.value:
			if self.left is not None:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None:
				self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMin()
				self.right.remove(self.value, self)
			elif p is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.right = self.right.right
					self.left = self.right.left
				else:
					# single node tree
					pass
			elif p.left == self:
				p.left = self.left if self.left is not None else self.right
			elif p.right == self:
				p.right = self.left if self.left is not None else self.right
		return self
	
	def getMin(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMin()
