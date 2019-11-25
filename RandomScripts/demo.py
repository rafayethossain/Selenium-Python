'''
Created on Nov 12, 2018

@author: Rafayet
'''

if __name__ == '__main__':
    pass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Chrome()
driver.get("http://www.google.com")
# assert "Google" in driver.title
print("Printing page title: "+ driver.title)
''' elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd) 
elem.send_keys(Keys.RETURN) '''
driver.close()
