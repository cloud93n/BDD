from selenium import webdriver
from selenium.webdriver import ChromeOptions
from helpers.helper_base import HelperFunc
 
def get_browser(browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        return HelperFunc(webdriver.Chrome("D:/chromedriver.exe",chrome_options=chrome_options))