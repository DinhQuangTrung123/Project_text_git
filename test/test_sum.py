import baitoan


def test_calculate_something():
    assert baitoan.calculate_something(3, 6) == 9
    assert baitoan.calculate_something(3, 6) == 10
    assert baitoan.calculate_something(3, 9) == 12
    assert baitoan.calculate_something(3, 7) == 10
