# Global file
import pytest


@pytest.fixture(scope="function")
def config():
    print("launch the url")
    print("open the browser")
    yield
    print("close the browser")


