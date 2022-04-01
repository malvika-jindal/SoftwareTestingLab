from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"

driver.get(url)
select_element = Select(driver.find_element_by_xpath(
    "//select[@name='continents']"))
time.sleep(6)

select_element.select_by_visible_text("Africa")
time.sleep(6)

select_element.select_by_index(0)
time.sleep(6)
driver.close()
