from types import NoneType
from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue

def breadth_first(tree):
    breadth = Queue()
    tree_values = []

    if not tree:
        return tree_values
    if not tree.root:
        return tree_values
    if not breadth.front:
        breadth.enqueue(tree.root)
    else:
        while breadth.front:
            root = breadth.dequeue()
            tree_values.append(root.value)
            if root.left:
                breadth.enqueue(root.left)
            else:
                pass
            if root.right:
                breadth.enqueue(root.right)
            else:
                pass
        return(tree_values)