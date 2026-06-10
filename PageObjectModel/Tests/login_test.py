from Actions.LoginActions import LoginActions
import pytest
from Utilities import logger

@pytest.mark.usefixtures("setupAndteardown")
class TestLogin:
    log = logger.log_generator()
    def test_validLogin(self):
        self.log.info("Test Started")
        logact = LoginActions(self.driver,self.wait)
        logact.login()
        self.log.info("Logged in")
        assert logact.checkingLogin()
        self.log.info("Asserted")
        print("Test Passed")
    