

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:/Users/Owner/chromedriver.exe')
driver.get('https://www.tangerine.ca/app/#/locations?locale=en_CA')
driver.find_element_by_id("abmSearch_searchField").send_keys("Toronto")
driver.find_element_by_xpath("""//*[@id="abmSearch_submitButton"]/span""").click()
k=driver.find_elements_by_class_name("location").text()

