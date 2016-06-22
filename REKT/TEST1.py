# vim:fileencoding=utf-8


#importy
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from glsdp import GLBaseTestCase
from glsdp import GLSupportUI
from glsdp import GLWait
from glsdp import GLHelper


#TestSearchForJob is class, that tests if after entering Rec-Global search site, and entering searchedPhrase
# into search box, you get any matches. If value returned (matches found) equals 0 then test is qualified as Failed

class TestSearchForJob(GLBaseTestCase, GLSupportUI):
    #preset driver and base url leading to Rec-global search site
    driverType = GLHelper.CHROME
    driverPath = "C:/Users/Gwozdo/Desktop/rek/chromedriver.exe"
    baseUrl = "http://www.rec-global.com/search?searchword=&ordering=newest&searchphrase=exact"
    # preset searched phrase in unicode
    searchedPhrase = u"QA Engineer"

    #definition of test case
    def testSearchForPhrase(self):
        #finding search box and pasting searchedPhrase into it
        self.findElementAndPutText(self.driver, By.XPATH, '//*[@id="search-searchword"]', self.searchedPhrase)

        #simply clicking 'Enter' button on search box element via submit method
        # (instead of manually clicking search button)
        element = self.driver.find_element_by_xpath('//*[@id="search-searchword"]')
        element.submit()

        #finding number of matches found element
        element2= self.driver.find_element_by_xpath('//*[@id="searchForm"]/div/p/strong/span')
        #asserting number of matches. if condition is true, test case is labeled as Failed
        self.assertFalse(element2.get_attribute("innerText") == "0")
        #printing result (number of matches found) if assertion part is passed
        print "Found " + element2.get_attribute("innerText")+ u" topics containing phrase: " + self.searchedPhrase



#Run the test
if __name__ == "__main__":
    unittest.main()