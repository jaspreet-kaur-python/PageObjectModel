import pytest
from conftest import obj_list
from pages.navigateToURL import navigatetoURL
from testresources import Constants
from testresources.readingdata import getdata, isRunnable

@pytest.mark.usefixtures("base_fixture")
class TestLogin:
    @pytest.mark.parametrize("argvals", getdata("test_login"))
    def test_Login(self, argvals):
        if(isRunnable("test_login")):
            if(argvals[Constants.RUNMODE_COL] == Constants.RUNMODE_Y):
                for i in range(0, len(obj_list)):
                    pass
                driver = obj_list[i].openbrowser(argvals[Constants.BROWSER])
                navigate = navigatetoURL(driver)
                welcomepage = navigate.gotourl()
                enterusername = welcomepage.welcomepage()
                enterpassword = enterusername.enterusername(argvals[Constants.USERNAME])
                homepage = enterpassword.enterpassword(argvals[Constants.PASSWORD])
                # if(homepage!=''):
                #     homepage.homepage()
                # else:
                #     obj_list[i].reportFailure("Username/Password incorrect")
            else:
                pytest.skip(Constants.DATASHEET_NO)
        else:
            pytest.skip(Constants.TESTCASESHEET_NO)

