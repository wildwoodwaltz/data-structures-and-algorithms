
class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def walk(root, data):
            if not root:
                return

            data.append(root.value)
            walk(root.left, data)
            walk(root.right, data)

        data_values = []
        walk(self.root, data_values)
        return data_values


    def in_order(self):
        def walk(root, data):
            if not root:
                return

            walk(root.left, data)
            data.append(root.value)
            walk(root.right, data)

        data_values = []
        walk(self.root, data_values)
        return data_values

    def post_order(self):
        def walk(root, data):
            if not root:
                return

            walk(root.left, data)
            walk(root.right, data)
            data.append(root.value)

        data_values = []
        walk(self.root, data_values)
        return data_values


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
