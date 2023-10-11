#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method

#CML commands to run test
#py.test -> it shows the test_demo1 passed or not.
#py.test -v (v stands for verbose) -> it provides more information
#py.test -v -s (Displays the logs) -> it prints the Hello result
#if you want to run only specific file then give py.test filename
import pytest

@pytest.mark.creditcard
def test_paymentCreditcard1():
    print("Hello")

#if we have same method name in pytest it will overrides the 1st method.
#but in other languagesit will report.
#here output will be "Good morning"
# def test_firdtprogram():
#     print("Good morning")

#In pytest every method(function) is treated as one test case

@pytest.mark.creditcard
def test_paymentDebitcard1(setup):
    print(1+1)
#What if you want to run one method from one file
#and 3 methods from 6 files and only 2 methods from 4files at a time?
# py.test -k Creditcard -s
