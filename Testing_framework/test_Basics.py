# Pytest Testing Framework .
import pytest


def test_signin(config):
    print("sign-in with valid credentials")



def test_ResetPassword():
    print("Click on the reset password button")

def test_login(config):
    print("click on the login button")







# @pytest.fixture(scope="module")
# def test_prework():
#     print('This is the scope function ,its executed parallely')
#
#
#
# @pytest.mark.smoke
# def test_postwork(test_prework):
#     print("browser closed")
#
# def test_boundary():
#     print("browser firefox")
# # def test_cricket(test_prework):
# #     print("cricket")
# # def test_football(test_prework):
# #     print("football")

# class - per class
#Function - execte for method

#Module - for file
#session - per session .

#pytest .mark,smoke
