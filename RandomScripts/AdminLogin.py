'''
Created on Nov 14, 2018

@author: Rafayet
'''


if __name__ == '__main__':
    pass

from selenium import webdriver
import time

#start_time = time.clock()
driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()

baseUrl ="http://dgda.qa:81/admin-login"
driver.get(baseUrl)

print("\nLoaded page: "+ driver.current_url)

#declaring elements

loginXpath ="/html/body/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[3]/div[2]/button"

print("\nLogin without inputting values")
time.sleep(3)
driver.find_element_by_xpath(loginXpath).click()


driver.refresh()
print("\nLogin with invalid user password")
driver.find_element_by_name("email").send_keys("mail@asad.net")
driver.find_element_by_name("password").send_keys("123456")
time.sleep(3)
driver.find_element_by_xpath(loginXpath).click()


driver.refresh()

print("\nLogin with valid user password")
driver.find_element_by_name("email").send_keys("asad@asad.net")
driver.find_element_by_name("password").send_keys("123456")
time.sleep(3)
driver.find_element_by_xpath(loginXpath).click()



# driver.find_element_by_name("email").send_keys("asad@asad.net")
#driver.find_element_by_name("password").send_keys("123456")

#driver.find_element_by_xpath(loginButton).click()

adminUrl = driver.current_url
print("\n Page after Login: "+ adminUrl)

expectedUrl = "http://dgda.qa:81/dashboard"

if adminUrl == expectedUrl:
    print("\nDesired URL found")
else:
    print("\nMismatch URL")
time.sleep(5)
print("\n Login out")
driver.find_element_by_xpath("//*[@id=\"navbar-mobile\"]/ul/li/a/strong").click()
driver.find_element_by_xpath("//*[@id=\"navbar-mobile\"]/ul/li/ul/li[7]/a").click()

print("\n")
print("Checking: if the dashboard is accessable after logged out\n")
driver.get(adminUrl)
if expectedUrl == driver.current_url:
    print("Accessible!")
else:
    print("Test success")

print("\nQuiting the system")
time.sleep(5)
driver.quit()
#print (time.clock() - start_time, "seconds")
