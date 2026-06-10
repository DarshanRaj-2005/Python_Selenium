from Actions.LoginActions import LoginActions
import pytest

@pytest.mark.usefixtures("setupAndteardown")
class TestLogin:
    def test_validLogin(self):
        logact = LoginActions()
        logact.driver = self.driver
        logact.wait = self.wait
        logact.login()
        assert logact.checkingLogin()
        print("Test Passed")