from pages.basepage import Base
from pages.welcomePage import WelcomePage


class navigatetoURL(Base):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def gotourl(self):
        self.navigate()
        self.validatetitle()
        return WelcomePage(self.driver)
