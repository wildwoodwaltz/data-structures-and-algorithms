from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_a, tree_b):
    list_ = BinaryTree.pre_order(tree_a)
    shared_numbers = []

    for num in list_:
        if tree_b.contains(num):
            shared_numbers.append(num)

    return shared_numbers
