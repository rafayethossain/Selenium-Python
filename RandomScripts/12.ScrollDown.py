from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#                                     Explaination
# in this tutorial we are going scroll down to the end of the page   



 

browser = webdriver.Chrome()
browser.get('https://wikipedia.org')

elm = browser.find_element_by_tag_name('html')
time.sleep(2)
elm.send_keys(Keys.END)


