from selenium import webdriver

class FirefoxTest():
    def test(self):
        # initiating webdriver
        driver = webdriver.Firefox()
        #opening url into the browser
        driver.get("https://www.google.com/")

Firefox = FirefoxTest()
Firefox.test()