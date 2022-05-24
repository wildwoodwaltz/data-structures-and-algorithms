import pytest
from merge_sort.merge_sort import merge_sort


def test_base_case():
    arr = [8,4,23,42,16,15]
    actual = merge_sort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sort():
    arr = [20,18,12,8,5,-2]
    actual = merge_sort(arr)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_same_numbers():
    arr = [5,12,7,5,5,7]
    actual = merge_sort(arr)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_close_to_sorted():
    arr = [2,3,5,7,13,11]
    actual = merge_sort(arr)
    expected = [2,3,5,7,11,13]
    assert actual == expected

def test_all_same():
    arr = [2,2,2,2,2]
    actual = merge_sort(arr)
    expected = [2,2,2,2,2]
    assert actual == expected


def test_negative_sort():
    arr = [-15,-12,-1,-22,-42,-55]
    actual = merge_sort(arr)
    expected = [-55,-42,-22,-15,-12,-1]
    assert actual == expected
