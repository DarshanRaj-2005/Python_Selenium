from Actions.SearchActions import SearchAction
from Utilities import logger
import pytest

@pytest.mark.usefixtures("setupAndteardown")
class TestSearch:

    log = logger.log_generator()
    def test_validsearch(self):
        self.log.info("Test Started")
        search = SearchAction(self.driver,self.wait)
        search.validSearch()
        self.log.info("Searched")
        assert search.checkingtext()
        self.log.info("Asserted the search")
        print("Test Passed")