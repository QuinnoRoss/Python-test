from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver');

driver.get("https://carmudi.com.ph")

assert driver.page_source.find(" <  "u"\u20B1" "500,000 ")
assert driver.page_source.find("  "u"\u20B1" "500,000 -  "u"\u20B1" "1,000,000 ")
assert driver.page_source.find("  "u"\u20B1" "500,000 -  "u"\u20B1" "1,000,000 ")
assert driver.page_source.find("> "u"\u20B1""2,000,000 ")

print ('Successfully asserted')







