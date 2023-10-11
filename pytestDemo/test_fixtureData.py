import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self,dataLoad): # we are passing paramater dataLoad because we are
        #getting the data from (conftest.py file method name dataLoad)
        #we are getting firstname, lastname and email to this method.
        print(dataLoad)
