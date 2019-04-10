#CherCherTech
# import the webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# set exe path and open the browser.
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver');

driver.get("https://google.com")

search = driver.find_element_by_name('q')
search.send_keys("carmudi")

search.send_keys(Keys.ENTER)

#browser.implicitly_wait(5)

click_link = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/a[1]/h3')
click_link.click()

driver.close()