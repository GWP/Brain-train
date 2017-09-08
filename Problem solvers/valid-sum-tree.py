#determine if a binary sum tree is a valid tree


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left_child(self, value):
        self.left = Node(value)

    def add_right_child(self, value):
        self.right = Node(value)


class BinarySumTree:

    def __init__(self, value):
        self.root = Node(value)

    def create(self, root, arrayOfValues, index):
        if arrayOfValues.length <= index:
            return 1

        if index == 0:
            self.root = Node(arrayOfValues[index])

        if arrayOfValues[2*index + 1] + arrayOfValues[2*index + 2] != arrayOfValues[index]:
            print("Invalid sum tree")
            return 0

        root.addLeftChild(arrayOfValues[2*index+1])
        root.addRightChild(arrayOfValues[2])

        self.create(root.left, arrayOfValues, 2*index+1)
        self.create(root.right, arrayOfValues, 2*index+2)

    def is_valid_sum_tree(self, root):
        if not root.left and not root.right:
            return True

        left = root.left or Node(0)
        right = root.right or Node(0)

        if left.value + right.value == root.value:
            return self.is_valid_sum_tree(left) and self.is_valid_sum_tree(right)

        else:
            return False
