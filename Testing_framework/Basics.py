# Pytest Testing Framework .
import pytest


@pytest.fixture(scope="module")
def test_prework():
    print('browser opened')



def test_postwork(test_prework):
    print("browser closed")

def test_boundary():
    print("browser firefox")
# def test_cricket(test_prework):
#     print("cricket")
# def test_football(test_prework):
#     print("football")

# class
#Function
#Module
#Class
