import pytest
from code_challenges.roman_numerals import numeral_converter


# @pytest.mark.skip("TODO")
def test_ones():
    numerals = 'I'
    actual = numeral_converter(numerals)
    expected = 1
    assert actual == expected

def test_fives():
    numerals = 'V'
    actual = numeral_converter(numerals)
    expected = 5
    assert actual == expected

def test_tens():
    numerals = 'X'
    actual = numeral_converter(numerals)
    expected = 10
    assert actual == expected

def test_fifties():
    numerals = 'L'
    actual = numeral_converter(numerals)
    expected = 50
    assert actual == expected

def test_hundreds():
    numerals = 'C'
    actual = numeral_converter(numerals)
    expected = 100
    assert actual == expected

def test_fivehundreds():
    numerals = 'D'
    actual = numeral_converter(numerals)
    expected = 500
    assert actual == expected

def test_Thousands():
    numerals = 'M'
    actual = numeral_converter(numerals)
    expected = 1000
    assert actual == expected

def test_year_number():
    numerals = "MMXXII"
    actual = numeral_converter(numerals)
    expected = 2022
    assert actual == expected

def test_numbers_before():
    numerals = "IX"
    actual = numeral_converter(numerals)
    expected = 9
    assert actual == expected

def test_numbers_after():
    numerals = "VII"
    actual = numeral_converter(numerals)
    expected = 7
    assert actual == expected

def test_wierd_numbers():
    numerals = 'IVLV'
    actual = numeral_converter(numerals)
    expected = 49
    assert actual == expected

def test_more_wierd_numbers():
    numerals = 'XLVIV'
    actual = numeral_converter(numerals)
    expected = 49
    assert actual == expected