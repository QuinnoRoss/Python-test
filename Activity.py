#CherCherTech
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# set exe path and open the browser.
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver');

URL = driver.get("https://www.carmudi.co.id/")


elem = driver.find_element_by_xpath('//div[@data-category="cars" and contains(text(),"< 100 Juta")]');
elem.click()

#ASSERT URL
assert driver.current_url.find("/cars/condition:all/price:-100000000/")

#VERIFIED NUM OF LISTINGS
number = len(driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]'))

a = 30;
if number == a:
  print "There are",number,"listings in the page 1"
elif a != number:
  print("fail")

#VERIFYING AMOUNT IF < 100
all_result = driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]')

for result in all_result:

	s = result.text
	q = s.split(" ")[0]
	#print float(q)		
if float(q) >= 100.0:
	print("Listing is greater 100 Juta in page 1!")
elif float(q) < 100:
	print("Listing is under than Juta in page 1")

time.sleep(5)

#CLICK FOR NEXT PAGE
driver.find_element_by_xpath('//a[@title="Halaman Selanjutnya"]').click();

time.sleep(5)
#PAGE 2 START
#ASSERT TITLE
assert driver.current_url.find("https://www.carmudi.co.id/cars/condition:all/price:-100000000/?page=2/")
#COUNT IF 30
number2 = len(driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]'))

a2 = 30;
if number2 == a2:
  print "There are",number2,"listings in the page 2"
elif a2 != number:
  print("fail")
#VERIFIED IF > 100 
all_result2 = driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]')

for result2 in all_result2:

	s2 = result2.text
	q2 = s2.split(" ")[0]
	#print(q2)	
if float(q2) >= 100.0:
	print("Listing is greater 100 Juta in page 2!")
elif int(q2) < 100:
	print("Listing is under 100 Juta in page 2")
#CLICK FOR NEXT PAGE
driver.find_element_by_xpath('//a[@title="Halaman Selanjutnya"]').click();

time.sleep(5)
#PAGE 3 START
#ASSERT TITLE
assert driver.current_url.find("https://www.carmudi.co.id/cars/condition:all/price:-100000000/?page=3/")
#COUNT IF 30
number3 = len(driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]'))
a3 = 30;
if number3 == a3:
  print "There are",number3,"listings in the page 3"
elif a3 != number:
  print("fail")
#VERIFIED IF > 100 
all_result3 = driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]')

for result3 in all_result3:

	s3 = result3.text
	q3 = s3.split(" ")[0]
		
if float(q3) >= 100.0:
	print("Listing is greater 100 Juta in page 3!")
elif float(q3) < 100:
	print("Listing is under 100 Juta in page 3")

#CLICK FOR NEXT PAGE
driver.find_element_by_xpath('//a[@title="Halaman Selanjutnya"]').click();
time.sleep(5)
#PAGE 4 START
#ASSERT TITLE
assert driver.current_url.find("https://www.carmudi.co.id/cars/condition:all/price:-100000000/?page=4/")
#COUNT IF 30
number4 = len(driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]'))
a4 = 30;
if number4 == a4:
  print "There are",number4,"listings in the page 4"
elif a4 != number:
  print("fail")
#VERIFIED IF > 100 
all_result4 = driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]')

for result4 in all_result4:

	s4 = result4.text
	q4 = s4.split(" ")[0]
	#print (q4)

if float(q4) >= 100.0:
	print("Listing is greater 100 Juta in page 4!")
elif float(q4) < 100:
	print("Listing is under 100 Juta in page 4")
#CLICK FOR NEXT PAGE
driver.find_element_by_xpath('//a[@title="Halaman Selanjutnya"]').click();

time.sleep(5)
#PAGE 4 START
#ASSERT TITLE
assert driver.current_url.find("https://www.carmudi.co.id/cars/condition:all/price:-100000000/?page=5/")
#COUNT IF 30
number5 = len(driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]'))
a5 = 30;
if number5 == a5:
  print "There are",number5,"listings in the page 5"
elif a5 != number:
  print("fail")
#VERIFIED IF > 100 
all_result5 = driver.find_elements_by_xpath('//p[@class="item-price type-xs price"]')

for result5 in all_result5:

	s5 = result5.text
	q5 = s5.split(" ")[0]
		
if float(q5) >= 100.0:
	print("Listing is greater 100 Juta in page 5!")
elif float(q5) < 100:
	print("Listing is under 100 Juta in page 5")

driver.close()






