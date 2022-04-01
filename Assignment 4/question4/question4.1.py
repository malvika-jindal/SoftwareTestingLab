from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://demoqa.com/select-menu"
driver.get(url)

dropdown = driver.find_element_by_xpath("//select[@id='oldSelectMenu']/option[text()='White']")
dropdown_select = dropdown.click()

driver.close()
