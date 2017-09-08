import unittest
import valid-sum-tree

class TestUM(unittest.TestCase):

    def setUp(self):
        bsumt = BinarySumTree(10)
        bsumt.root.addLeftChild(4)
        bsumt.root.addRightChild(6)
        lt = bsumt.root.left
        rt = bsumt.root.right
        lt.addLeftChild(2)
        lt.addRightChild(2)
        rt.addLeftChild(6)

