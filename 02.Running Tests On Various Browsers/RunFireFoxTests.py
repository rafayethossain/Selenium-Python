'''
You will be needing this time geckowebdriver instead of chromedriver
and all the other reequirements are the same
'''

from selenium import webdriver


url = "http://www.google.com"
driver = webdriver.Firefox()

#driver.quit()



driver.get(url)

