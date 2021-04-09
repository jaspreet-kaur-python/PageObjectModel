import logging
from _datetime import datetime
from _overlapped import NULL

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest
import allure

from testresources import Constants


class Base:
    def __init__(self):
        self.prod = conftest.prod
        self.log = logging.getLogger()
        self.driver = NULL

#opens browser dynamically
    def openbrowser(self, browsername):
        with allure.step("Opening browser - "+browsername):
            if(self.prod['GridRun'] == Constants.RUNMODE_Y):
                if (browsername == Constants.CHROME):
                    caps = DesiredCapabilities.CHROME.copy()
                    caps['browserName'] = 'chrome'
                    caps['javascriptEnabled'] = True
                elif (browsername == Constants.FIREFOX):
                    caps = DesiredCapabilities.FIREFOX.copy()
                    caps['browserName'] = 'firefox'
                    caps['javascriptEnabled'] = True
                elif (browsername == Constants.EDGE):
                    caps = DesiredCapabilities.EDGE.copy()
                    caps['browserName'] = 'MicrosoftEdge'
                    caps['javascriptEnabled'] = True
                else:
                    caps = DesiredCapabilities.INTERNETEXPLORER.copy()
                    caps['browserName'] = 'internet explorer'
                    caps['javascriptEnabled'] = True
                try:
                    self.driver = webdriver.Remote(desired_capabilities=caps,
                                                   command_executor='http://192.168.0.101:4444/wd/hub')
                except Exception as e:
                    print(e)
            else:
                if(browsername==Constants.CHROME):
                    self.driver = webdriver.Chrome()
                elif(browsername==Constants.FIREFOX):
                    self.driver = webdriver.Firefox()
                elif(browsername==Constants.EDGE):
                    self.driver = webdriver.Edge()
                else:
                    self.driver = webdriver.Ie()
            self.takescreenshot()
            return self.driver

    def navigate(self):
        with allure.step("Navigating to - "+self.prod['URL']):
            self.driver.get(self.prod['URL'])
            self.takescreenshot()

    def clickOnElement(self, obj):
        with allure.step("Clicking on - "+obj):
            if(self.getElement(obj)!=''):
                self.getElement(obj).click()
                self.takescreenshot()

    def type(self, obj, data):
        with allure.step("Typing in - " + obj+" with "+data):
            if (self.getElement(obj)!=''):
                self.getElement(obj).send_keys(data)
                self.takescreenshot()

    def quitbrowser(self):
        if(self.driver!=NULL):
            self.driver.quit()

    def isElementPresent(self, key):
        wait = WebDriverWait(self.driver, 10)
        element = self.prod[key]
        if(key.endswith('_id')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.ID, element)))
        elif (key.endswith('_xpath')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.XPATH, element)))
        elif (key.endswith('_name')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.NAME, element)))
        elif(key.endswith('_cssSelector')):
            elementlist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            print("No element found")

        if(len(elementlist)==0):
            return False
        else:
            return True

    def isElementVisible(self, key):
        wait = WebDriverWait(self.driver, 10)
        element = self.prod[key]
        if (key.endswith('_id')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.ID, element)))
        elif (key.endswith('_xpath')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.XPATH, element)))
        elif (key.endswith('_name')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.NAME, element)))
        elif (key.endswith('_cssSelector')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            print("No element found")

        if (len(elementlist) == 0):
            return False
        else:
            return True

    def getElement(self, key):
        if(self.isElementPresent(key) and self.isElementVisible(key)):
            try:
                if (key.endswith('_id')):
                    element = self.driver.find_element_by_id(self.prod[key])
                elif (key.endswith('_xpath')):
                    element = self.driver.find_element_by_xpath(self.prod[key])
                elif (key.endswith('_name')):
                    element = self.driver.find_element_by_name(self.prod[key])
                elif(key.endswith('_cssSelector')):
                    element = self.driver.find_element_by_css_selector(self.prod[key])
                else:
                    return ''
                return element
            except Exception as e:
                print(e)
                print("Element not found")
        else:
            print("Element either not present or visible")

    def validatetitle(self):
        with allure.step("Validating title...."):
            #actual value - self.driver.title
            #expected value - properties.file
            actualtitle = self.driver.title
            expectedtitle = self.prod['homepagetitle']
            if(actualtitle==expectedtitle):
                # self.reportSuccess("Title matched")
                self.infologs("Title matched")
            else:
                # self.reportFailure("Title did not matched")
                self.infologs("Title did not matched")

    def takescreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot captured at : " + str(datetime.now()),
                      AttachmentType.PNG)

    def reportFailure(self, msg):
        self.errorlogs(msg)
        assert False

    def reportSuccess(self, msg):
        self.infologs(msg)
        assert True

    def infologs(self, msg):
        self.log.setLevel(logging.INFO)
        self.log.info(msg)

    def errorlogs(self, msg):
        self.log.setLevel(logging.ERROR)
        self.log.error(msg)