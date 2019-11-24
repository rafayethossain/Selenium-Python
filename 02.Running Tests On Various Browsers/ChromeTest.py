
from selenium import webdriver

class ChromeTest():
    def test(self):
        # initiating webdriver
        driver = webdriver.Chrome()
        #opening url into the browser
        driver.get("https://www.google.com/")

Chrome = ChromeTest()
Chrome.test()