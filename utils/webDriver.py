from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import elements
import time

class webDriver():
    def __init__(self,):
        self.driver = webdriver.Chrome(options=self.get_browser_options())

    def get_browser_options(self):
        options = Options()
        # options.add_argument("--start-maximized")
        # options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-gpu")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")

        options.add_argument("--disable-dev-shm-usage")

        # options.add_argument("--headless")

        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")

        options.add_argument("--disable-extensions")
        prefs = {"download.default_directory" : os.getcwd() + "/db/Files/downloads"}

        options.add_experimental_option("prefs", prefs)

        return options

    def sendEnter(self, xpathValue: Any) -> None:
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, xpathValue).send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
        
    def get(self, url: str):
        self.driver.get(url)

    def element(self, xpathValue: Any, element = None):
        # time.sleep(1)
        try:
            if element is None:
                return self.driver.find_element(By.XPATH, xpathValue)
            else:

                element = element.find_element(By.XPATH, xpathValue)
                return element
        except Exception as e:
            if xpathValue not in (elements.listProperties_Page_Badge, elements.pageNext, elements.listProperties_Page_Beds):
                print("xpathValue" + "-- >", xpathValue)
            return None

    def click(self, xpathValue: Any):
        time.sleep(1.1)
        try:
            # element = self.wait_for_element(xpathValue)
            self.element(xpathValue).click()
            return True
        except Exception as e:
            print(e)
            return False

    def send_text(self, xpathValue: Any, text: str):
        try:
            input_field = self.element(xpathValue)
            input_field.clear()
            input_field.send_keys(text)
        except Exception as e:
            print(e)

    def wait_for_element(self, xpathValue: Any, element = None, timeout = 10):
        try:
            if element is None:
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((By.XPATH, xpathValue)))
                return element
            else:
                element = WebDriverWait(element, timeout).until(EC.visibility_of_all_elements_located((By.XPATH, xpathValue)))
                return element
        except Exception as e:
            print(e)
        return None
    def actualElement(self, xpathList: Any):
        for element in xpathList:
            try:
                el = self.element(element)
                if el is not None:
                    return el
            except Exception as e:
                print(e)
        return None

    def findElements(self, xpathValue: Any, element = None):
        try:
            if element is None:
                elements = self.driver.find_elements(By.XPATH, xpathValue)
                return elements
            else:
                elements = element.find_elements(By.XPATH, xpathValue)
                return elements
        except Exception as e:
            print(e)
            return None

    def close(self):
        self.driver.close()

    def quit(self):
        '''shut down the browser and close all tabs'''
        self.driver.quit()

    def __call__(self):
        return self.driver

