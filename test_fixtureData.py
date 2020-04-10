import pytest

from BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoading")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoading):
        log = self.getLogger
        log.info(dataLoading[0])
        log.info(dataLoading[1])
        print(dataLoading[1])
