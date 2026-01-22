import pytest


def test_core( config):
    print("Core Module")
@pytest.mark.smoke
def test_Sales():
    print("sales Module")
    return "pass"

def test_finance(test_sales):
    print("Finance Module")
    assert test_sales == "pass"
