from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        super().__init__()

    def add(self, value):

        node = Node(value)

        def walk(root, new_node):
            if not root:
                return

            new_value = new_node.value

            if new_value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node

            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        if not self.root:
            self.root = node
            return

        walk(self.root, node)


    def contains(self, value):
        def walk(root, value):
            if not root:
                return False

            return (root.value == value or walk(root.left, value) or walk(root.right, value))

        return walk(self.root, value)

    # def contains(self,value):
        
    #     def walk(root, value):

    #         if value == root.value:
    #             return True

    #         elif root.value != value:

    #             if root.value > value:
    #                 if root.left is None:   
    #                     return False
    #                 walk(root.left, value)

    #             if root.value < value:
    #                 if root.right is None:
    #                     return False
    #                 walk(root.right,value)

    #     walk(self.root, value)

