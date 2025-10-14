import pytest
from leap_year import leap_year

def test_1997_is_not_a_leap_year():
    assert leap_year(1997) == False

def test_1996_is_a_leap_year():
    assert leap_year(1996) == True

def test_1600_2000_is_a_leap_year():
    assert leap_year(2000) == True
    assert leap_year(1600) == True

def test_1800_is_not_a_leap_year():
    assert leap_year(1800) == False

def test_string_input_rejected_gracefully():
    assert leap_year('year') == False

def test_numbers_as_string_processed():
    assert leap_year('1997') == False
    assert leap_year('2024') == True

def test_floats_are_processed():
    assert leap_year(1997.0) == False
    assert leap_year(1984.0) == False