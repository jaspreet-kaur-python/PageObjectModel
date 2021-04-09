from pages.basepage import Base
from pages.usernameDetailsPage import UsernameDetails


class WelcomePage(Base):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def welcomepage(self):
        self.clickOnElement('loginlink_xpath')
        return UsernameDetails(self.driver)
