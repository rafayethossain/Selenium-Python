#Getting all url from a page and export into a text file
from selenium import webdriver
import requests 
import time

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

driver.get("http://mis.totthoapa.gov.bd/TotthoApa")


driver.close()

 
   
        
         
