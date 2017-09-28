

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:/Users/Owner/chromedriver.exe')
#cities=("Ottawa","Montreal","Waterloo","Kitchener","Missisauga","Hamilton","Cambridge","Guelph","Windsor","London")
driver.get('https://www.tangerine.ca/app/#/locations?locale={cities_list})
driver.find_element_by_id("abmSearch_searchField").send_keys("{cities_list}")
driver.find_element_by_xpath("""//*[@id="abmSearch_submitButton"]/span""").click()
k=driver.find_elements_by_class_name("location").text()
for i in range(1,len(k)):
    k=c[i].get_attribute("innerHTML")
    print(k)
with open('qwe.txt', 'w') as f:
    print(k, file=f)

import geocoder
with open("qwe.txt",'r') as fp:
    for line in fp:
        try:
            g= geocoder.google(line)
            print(g.address,g.latlng)
        except:
            print(0,0)
fp.close()

