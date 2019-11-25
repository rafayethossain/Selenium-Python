from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://google.com")
assert('Google' in driver.title)