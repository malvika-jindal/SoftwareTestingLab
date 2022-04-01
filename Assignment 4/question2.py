from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.facebook.com")

email = driver.find_element_by_id('email')
email.send_keys("example@gmail.com")
pswd = driver.find_element_by_id('pass')
pswd.send_keys("password")

login = driver.find_element_by_name('login')
login.click()
print('Invalid log in')
