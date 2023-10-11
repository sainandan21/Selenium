import pytest
@pytest.fixture()#if we pass scope = "class", then
#output will be I will be executing first
#it will execute all the methods in the class and then only it will go to nextstep of the yield
#I will be executed last.

#ex: if we use scope="class" and we have 3 methods in that class addtion method, sub method
#multiply method

#I will be executing first
#2 -> additions output
#1 -> sub ouput
#8 -> mul outuput
#I will be executed last

# _________________________________________

#what if we dont give scope="class"
#I will be executing first
#2 -> additions output
#I will be executed last

#I will be executing first
#1 -> sub ouput
#I will be executed last
#8 -> mul outuput
#I will be executing first

#I will be executed last
def setup():
    print("I will be executing first") #connect to database
    yield
    print("I will be executed last") #terminate the database connection.

def dataLoad():
    print("User details is being created")
    return ["Sai","M","sm13@gmail.com"]

#Parameterizing test with mulitple data sets using fixtures
#if you want to run your test with multiple browsers


#this param, it will pass chrome as an 1st input and then firefox as 2nd input and IE as 3rd input
#each time one will be picked and it will to paramater as request.
@pytest.fixture(params=["chrome","firefox","IE"])

def crossBrowser(request):
    return request.param

#@pytest.fixture(params=[("chrome","abc","Abc123),("firefox","1.2323.1"),"IE"])
#here it treat as a one parameter-> ("chrome","abc","Abc123)