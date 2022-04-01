from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# URL of website
url = "https://selenium-python.readthedocs.io/locating-elements.html"

# Opening the website
driver.get(url)

# executing js by scrolling the window
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")

time.sleep(5)
driver.close()
