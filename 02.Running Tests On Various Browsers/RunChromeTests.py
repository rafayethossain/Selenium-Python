'''
Before running this code you must have these following thing in PC
1. If required Python version is istall properly

2. Chrome webdriver is placed in the in proper PATH
mine is in 

C:/Users/AppData/Local/Programs/Python/Python37-32/Scripts the location

3. Chrome browser version and webdriver version matched

4. OS bit version should be same 32 bits / 64 bits 

'''

from selenium import webdriver


url = "http://www.google.com"
driver = webdriver.Chrome()

#driver.quit()



driver.get(url)

