import pytest

#Here setup is passed as a parameter to test_fixtureDemo
#it will call setup -> I will be executing first
#yield-> temporary break to that function. it will go to test_fixtureDemo and calls
#I will be executed last
#next it will go previous function and print i will executed last.
# @pytest.fixture()
# def setup():
#     print("I will be executing first") #connect to database
#     yield
#     print("I will be executed last") #terminate the database connection.

def test_fixturesDemo(setup):
    print("I will execute steps in fixtureDemo method") #retrive all details
    #from database

#what if we need to connect database for remaning testcases in different files ?
# to avoid the dublicate code, we can use confitest -> it is a filename and it will available
#to all files.

#we can move setup function to that confitest.py
