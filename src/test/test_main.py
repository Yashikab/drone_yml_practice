# python3.7.5
import pytest
from module.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("target_num, expected", [
    (3, 'fizz'),
    (5, 'buzz'),
    # (7, '7'),
    (30, 'fizzbuzz')
])
def test_fizzbuzz(target_num, expected):
    assert fizzbuzz(target_num) == expected
