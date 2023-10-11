import pytest
#easiest way to pass setup in required method.
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("fixture1")

    def test_fixtureDemo2(self):
        print("fixture2")

    def test_fixtureDemo3(self):
        print("fixture3")
