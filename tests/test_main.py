from src.main import divide, calculate_log, reverse_string
import pytest

def test_divide():
    assert divide(1, 1) == 1

    assert divide(2, 0) == 0


def test_calc_log():
    assert calculate_log(8, 2) == 3.0

    with pytest.raises(ValueError):
        calculate_log(0, 2)

    with pytest.raises(ValueError):
        calculate_log(2, 0)


@pytest.mark.parametrize('value, expected',[
                         ('123', '321'),
                         ('hello', 'olleh'),
                         ('world', 'dlrow')
                         ])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected

# def test_reverse_string_numbers(numbers):
#     assert reverse_string('123') == numbers
#
#
# def test_reverse_string_letters(letters):
#     assert reverse_string('hello') == letters

