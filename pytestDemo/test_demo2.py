import pytest

#To skip any testcase that has bug and need to fix afterwards then use
#@pytest.mark.skip
@pytest.mark.creditcard
@pytest.mark.skip
def test_paymentCreditcard2():
    msg = "Hello, everyone"
    # assert msg in "He","Test Failed"
    print(msg)
    # if test passed it will give log has True or else it will
    # give as False and also it will provide assertionError: Test failed.
    #Then use py.test -k Creditcard (k means regular expression so, it will seacrh
    # all methods which conatins Creditcard text.)
@pytest.mark.messages
def test_logoutMessage():
    message = "Good bye!"
    print(message)

@pytest.mark.messages
def test_creditcardFailure():
    print("Invalid details")

#How to run only creditcard test but not creditcardFailure test.
#Then we can use mark concept
#py.test -m creditcard -s

#To skip any testcase that has bug and need to fix afterwards then use
#@pytest.mark.skip


#if this testcase has some bugs but this method contains operations that are used in another method
# still you want to run this test case but skip this report/message in our console.
#then use xfail
#@pytest.mark.xfail

#THIS IS A UNIQUE ANOTATION THAT IS NOT PRESENTED IN ANY TESTING FRAMEWORK
@pytest.mark.xfail
def test_login():
    print("login details")

def test_mulitpleData(crossBrowser):
    print(crossBrowser[0]) #it will print-> chrome







