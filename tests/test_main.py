from src.main import divide
from src.main import calculate_log as calc_log


def test_divide():
    assert divide(1, 1) == 1

    assert divide(2, 0) == 0


def test_calc_log():
    assert calc_log(8, 2) == 3.0



