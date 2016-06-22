# vim:fileencoding=utf-8
# Copyright (c) GlobalLogic.

__version__ = "0.1"
__author__ = "Damian Giebas"

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from glsdp import GLBaseTestCase
from glsdp import GLHelper

class NavigateToPage(GLBaseTestCase):
    driverType = GLHelper.CHROME
    driverPath = "C:/Users/Gwozdo/Desktop/rek/chromedriver.exe"
    def glBeforeSetUp(self):
        print "Starting the webdriver"

    def glAfterSetUp(self):
        print "Webdriver has been started"

    def glBeforeTearDown(self):
        print "Starting off the driver"

    def glAfterTearDown(self):
        print "Drive has been closed"

    def testLoadingPage(self):
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//div[@id='pageloader']")
            )
        )

if __name__ == "__main__":
    unittest.main()