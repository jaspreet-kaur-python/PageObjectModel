from pages.basepage import Base
from pages.zohohomepage import ZohoHomePage


class PasswordDetails(Base):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterpassword(self, password):
        self.type('passwordtxtbox_xpath', password)
        self.clickOnElement('signbtn_xpath')
        # if(self.isElementPresent('crmlink_xpath')):
        #     #return obj of next page
        #     return ZohoHomePage()
        # else:
        #     self.errorlogs("Username/Password incorrect")


#grid server
#configure hub machine
#configure node machine -

#code change in open browser