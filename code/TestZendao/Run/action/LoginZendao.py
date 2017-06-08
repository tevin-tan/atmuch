import locator
from selenium import webdriver


class login():
    driver = None
    def __init__(self):
        Browser = webdriver.Firefox()
        # Browser.maximize_window()
        Browser.get(locator.url)
        
        Browser.find_element_by_xpath(locator.locate['username']).send_keys("admin")
        Browser.find_element_by_xpath(locator.locate['password']).send_keys("123456")
        Browser.find_element_by_xpath(locator.locate['login']).click()
        
        self.driver = Browser
        
    def login_browser(self):
        return self.driver 
    
# def Login():   
#     Browser = webdriver.Firefox()
#     # Browser.maximize_window()
#     Browser.get(locator.url)
#     
#     Browser.find_element_by_xpath(locator.locate['username']).send_keys("admin")
#     Browser.find_element_by_xpath(locator.locate['password']).send_keys("123456")
#     Browser.find_element_by_xpath(locator.locate['login']).click()
#    
#     return Browser
