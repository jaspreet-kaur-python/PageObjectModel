import time

from pages.basepage import Base
from pages.passwordDetailsPage import PasswordDetails


class UsernameDetails(Base):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterusername(self, username):
        self.type('usernametxtbox_name', username)
        self.clickOnElement('nextbtn_xpath')
        time.sleep(5)
        return PasswordDetails(self.driver)


