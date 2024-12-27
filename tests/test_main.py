from src.main import divide


def test_divide():
    assert divide(1, 1) == 1

    assert divide(2, 0) == 0
     
