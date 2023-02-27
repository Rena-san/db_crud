import pytest


@pytest.mark.usefixtures("set_up_1", "close_connect")
class TestSuit:
    def test_case_1(self):
        assert (1 + 2) == 3
