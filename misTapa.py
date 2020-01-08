from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FirefoxTest():
    def test(self):
        # initiating webdriver
        driver = webdriver.Firefox()
        #opening url into the browser
        driver.get("http://mis.totthoapa.gov.bd/totthoapa")
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin@123")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dpdaf")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='পাসওয়ার্ড'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//*/text()[normalize-space(.)='5. Payroll Management System']/parent::*").click()
        driver.find_element_by_link_text("Task").click()
        driver.find_element_by_link_text("Employee Salary Structure").click()
        driver.find_element_by_link_text("pd").click()
        driver.find_element_by_link_text("Salary Structure").click()
        driver.find_element_by_id("NextEmployee").click()

        for i in range(2000):
            try:
                element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "NextEmployee")))
                driver.find_element_by_id("NextEmployee").click()
                driver.implicitly_wait(10)
                driver.find_element_by_id("btnCreate").click()
                driver.implicitly_wait(10)
            finally:
                print("hello")
                

Firefox = FirefoxTest()
Firefox.test()
 
