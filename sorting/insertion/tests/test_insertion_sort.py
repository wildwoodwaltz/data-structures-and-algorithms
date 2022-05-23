
import pytest
from insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
    arr = [2,1,17,83,28,13]
    actual = insertion_sort(arr)
    expected = [1,2,13,17,28,83]
    assert actual == expected