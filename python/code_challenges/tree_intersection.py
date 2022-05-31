from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable



def tree_intersection(tree_a, tree_b):
    shared_numbers = []

    table_a = Hashtable()
    for num in tree_a.post_order():
        print(num)
        table_a.set(num, num)
        
    for num in tree_b.post_order():
        if table_a.contains(num):
            if num in shared_numbers:
                pass
            else:
                shared_numbers.append(num)

    return shared_numbers
