import pytest


@pytest.mark.parametrize("mul, expected", [(1 * 2, 2), (2 * 2, 4), (3 * 2, 6)])
@pytest.mark.usefixtures("set_up_2", "close_connect")
class TestSuit:
    def test_case_2(self, mul, expected):
        assert mul == expected
