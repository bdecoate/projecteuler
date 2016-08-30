# 							75
# 						  95 64
# 						17 47 82
# 					  18 35 87 10
# 					20 04 82 47 65
# 				  19 01 23 75 03 34
# 				88 02 77 73 07 63 67
# 			  99 65 04 28 06 16 70 92
# 			41 41 26 56 83 40 80 70 33
# 		  41 48 72 33 47 32 37 16 94 29
# 		53 71 44 65 25 43 91 52 97 51 14
# 	  70 11 33 28 77 73 17 78 39 68 17 57
# 	91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
import sys
import attr


@attr.s
class Node(object):
	"""A pyramid node class to create a tree

	:val: the numeric value of the node
	:left: the left child, None if leaf
	:right: the right child, None if leaf
	:path_sum: this nodes' greatest path sum
	"""
	val = attr.ib()
	left = attr.ib()
	right = attr.ib()
	path_sum = attr.ib()


class PathSum(object):
	def __init__(self, pyramid):
		self._table = {}
		self._pyramid = pyramid

	def solve(self):
		"""Solve all path sums for the pyramid

		Calculate path sums from the bottom up, storing the values of sub paths
		that have already been caluclated to reuse these solutions
		"""
		# reverse enumerator for the pyramid
		flipped_pyramid = zip(
			reversed(range(len(self._pyramid))),
			reversed(self._pyramid))

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


try:
	filename = sys.argv[1]
except IndexError:
	filename = 'triangle.txt'

with open(filename, 'r') as numbers_file:
	pyramid = [map(int, line.strip('\n').split(' ')) for line in numbers_file]

solution = PathSum(pyramid)
print solution.solve()
