import sys


class Node(object):
	def __init__(self, val, left, right, path_sum):
		self.val = val
		self.left = left
		self.right = right
		self.path_sum = path_sum


class PathSum(object):
	def __init__(self, pyramid):
		self._table = {}

	def solve(self):
		"""Solve all path sums for the pyramid

		Calculate path sums from the bottom up, storing the values of sub paths
		that have already been caluclated to reuse these solutions
		"""
		# reverse enumerator for the pyramid
		flipped_pyramid = zip(
			reversed(range(len(pyramid))),
			reversed(pyramid))

		for i, row in flipped_pyramid:
			self._table[i] = []
			for j, val in enumerate(row):
				try:
					left = self._table[i + 1][j]
					right = self._table[i + 1][j + 1]
					path_sum = None
				except KeyError:  # expect KeyError for the leaf nodes
					left = None
					right = None
					path_sum = val

				# Add the node to the table, and calculate its max path_sum
				self._table[i].append(Node(val, left, right, path_sum))
				self.path_sum(i, j)
				return self.path_sum(0, 0)

	def path_sum(self, i, j):
		"""Calculate a node's pathsum

		If the pathsum has already been calculated, just return it
		"""
		node = self._table[i][j]
		if node.path_sum is None:
			node.path_sum = self._path_sum(node)
			return node.path_sum

	def _path_sum(self, node):
		"""Recursively calculate a node's pathsum

		If a sub-path sum has already been calculated,
		the calculation for that subpath stops there
		"""
		if node.path_sum is None:
			left_sum = self._path_sum(node.left)
			right_sum = self._path_sum(node.right)
			return node.val + max(left_sum, right_sum)
		else:
			return node.path_sum


num_test_cases = int(sys.stdin.readline().strip('\n'))
for i in range(num_test_cases):
	num_rows = int(sys.stdin.readline().strip('\n'))
	pyramid = [map(int, sys.stdin.readline().strip('\n').split(' ')) for _ in range(num_rows)]
	solution = PathSum(pyramid)
	print solution.solve()
