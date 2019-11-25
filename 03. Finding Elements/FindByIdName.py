from selenium import webdriver

class FindByName():
    def test(self):
        driver = webdriver.Chrome()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)
        findByNameResult = driver.find_element_by_name("enter-name")

        if findByNameResult is not None:
            print("Element found!")
        else:
            print("Not found!")

testObj = FindByName()
testObj.test()
