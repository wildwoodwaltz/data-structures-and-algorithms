import pytest
from data_structures.binary_tree import BinaryTree
from code_challenges.tree_intersection import tree_intersection


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():
    tree_a = BinaryTree()
    tree_b = BinaryTree()

    values_a = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    values_b = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]

    for num_a in values_a:
        tree_a.add(num_a)
    for num_b in values_b:
        tree_b.add(num_b)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)
