import unittest
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def return_size(self):
		return self.get_size(self.root)

	def get_size(self, root):
		if root == None:
			return 0
		else:
			return 1+self.get_size(root.left)+self.get_size(root.right)

	def return_search(self, data):
		return self.search(self.root, data)

	def search(self, root, data):
		if root == None:
			return False
		if root.data == data:
			return True
		elif data > root.data:
			return self.search(root.right, data)
		else:
			return self.search(root.left, data)

	def return_insert(self, data):
		if self.root:
			return self.insert(self.root, data)
		else:
			self.root = Node(data)
			return True

	def insert(self, root, data):
		if root.data == data:
			return False
		elif data < root.data:
			if root.left:
				return self.insert(root.left, data)
			else:
				root.left = Node(data)
				return True
		else:
			if root.right:
				return self.insert(root.right, data)
			else:
				root.right = Node(data)
				return True

	def preorder_traversal(self, root):
		if root:
			print(str(root.data), end='')
			self.preorder_traversal(root.left)
			self.preorder_traversal(root.right)

	def postorder_traversal(self, root):
		if root:
			self.postorder_traversal(root.left)
			self.postorder_traversal(root.right)
			print(str(root.data),end='')

	def inorder_traversal(self, root):
		if root:
			self.inorder_traversal(root.left)
			print(str(root.data),end='')
			self.inorder_traversal(root.right)


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.return_insert(10)
        self.tree.return_insert(15)
        self.tree.return_insert(6)
        self.tree.return_insert(4)
        self.tree.return_insert(9)
        self.tree.return_insert(12)
        self.tree.return_insert(24)
        self.tree.return_insert(7)
        self.tree.return_insert(20)
        self.tree.return_insert(30)
        self.tree.return_insert(18)

    def test_search(self):
        self.assertTrue(self.tree.return_search(24))
        self.assertFalse(self.tree.return_search(50))

    def test_size(self):
        self.assertEqual(11, self.tree.return_size())

if __name__ == '__main__':
    unittest.main()
