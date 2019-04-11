from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver');

driver.get("https://carmudi.com.ph")

element = driver.find_element_by_xpath('//*[@id="c-budget-container-cars"]/div[1]')
assert "500" in element.text

sec_element = driver.find_element_by_xpath('//*[@id="c-budget-container-cars"]/div[2]')
assert "1,000,000" in sec_element.text

th_element = driver.find_element_by_xpath('//*[@id="c-budget-container-cars"]/div[3]')
assert "2,000,000" in th_element.text

f_element = driver.find_element_by_xpath('//*[@id="c-budget-container-cars"]/div[4]')
assert ">" in f_element.text

print ('Successfully asserted '+element.text) 
print ('Successfully asserted '+sec_element.text)
print ('Successfully asserted '+th_element.text)
print ('Successfully asserted '+f_element.text)