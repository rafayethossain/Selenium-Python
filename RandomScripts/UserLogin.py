from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()

baseUrl ="http://dgda.qa:81"
driver.get(baseUrl)

print("\nCurrent page link: "+driver.current_url)
print("\n Navigating to login page")

driver.find_element_by_link_text("Login").click()
print("\nCurrent page link: "+driver.current_url)

loginXpath ="/html/body/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[3]/div[2]/button"

print("\nLogin without inputting values")
time.sleep(3)
driver.find_element_by_id("login-submit").click()


 
print("\nLogin with invalid user password")
driver.find_element_by_id("email").send_keys("mail@asad.net")
driver.find_element_by_id("password").send_keys("123356")
time.sleep(3)
driver.find_element_by_id("login-submit").click()

 
time.sleep(3)
print("\nLogin with valid user password")
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("asad@asad.net")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
time.sleep(3)
driver.find_element_by_id("login-submit").click()
print("\nCurrent page link: "+driver.current_url)


expectedUrl = "http://dgda.qa:81/home"

adminUrl = driver.current_url
print("\n Page after Login: "+ adminUrl)


if adminUrl == expectedUrl:
    print("\nDesired URL found")
else:
    print("\nMismatch URL")
time.sleep(5)


print(" \n Page Title right before switching language: " + driver.title)

# "Adverse Drug Reaction Reporting - Directorate General of Drug Administration (DGDA)"

driver.find_element_by_xpath(" /html/body/div[1]/div[1]/div/div/div[2]/nav/ul/li[1]").click()
webtitle = driver.find_element_by_xpath("//*[@id=\"main-nav\"]/div[1]/a/span/h1").text
expectedTitle ="ADVERSE DRUG REACTION REPORTING"

if webtitle == expectedTitle:
    print("\nMatched with expected title")
else:
    print("\n Title mismatch")

print("\nQuiting the system")
time.sleep(5)
driver.quit()
