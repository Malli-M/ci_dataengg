import pytest
from process_data import add_one_to_values

def test_add_one_to_values():
    assert add_one_to_values([1, 2, 3]) == [2, 3, 4]
    assert add_one_to_values([0, 0, 0]) == [1, 1, 1]
    assert add_one_to_values([-1, -2, -3]) == [0, -1, -2]
