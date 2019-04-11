# PYTHON

## Hello World

* Open terminal
* Enter the command `mkdir%NAME%` **(name representing the name of the file)**
* Enter the name of the directory
* Enter the command `subl .` **(opens sublime text editor)**
* Create a new file
* Type ` print ' Hello World! ', `
* Save the file and name it "name.py" 
* Go back to terminal
* Click ctrl + c
* Type the command `python name.py`

## Hello World Via Local Host

* Open terminal
* Enter the name of your directory **(e.g python-test)**
* Enter the command `subl .` **(open sublime text editor)**
* Create a new file
* Open your browser 
* Navigate to "https://www.acmesystems.it/python_http"
* Copy the code under 'example1.py'
* Go back to your newly created file
* Paste the code
* Save the file and name it "name.py"
* Go back to terminal 
* Click ctrl + c
* Enter the command `python name.py`
* Open browser 
* Navigate to "http://localhost:8080/"

## Opening browser via selenium

* Open terminal
* Enter the command `pip install selenium` **(installing selenium)**
* Enter the command `wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz` **(install geckodriver)**
* Enter the command `tar -xvzf geckodriver*`    **(unzipping geckodriver)**
* Enter the command `chmod +x geckodriver`  **(making the geckodriver as an executable file)**
* Enter the command `sudo mv geckodriver /usr/local/bin/`   **(moving the geckodriver to a different location)**
* Go back to terminal
* Enter the command `mkdir%NAME%` **(name representing the name of the file)**
* Enter the name of the directory
* Enter the command `subl .`
* Create a new file
* Open your browser
* Navigate to "https://chercher.tech/python/browser-commands"
* Look for the "open Firefox in selenium python" section
* Paste the code in your created file
* Copy the code
* Save the code and name it "name.py"
* Go back to terminal
* Enter the command `python name.py`

## Asserting texts in the website
*
* Open terminal
* Enter the command `mkdir %NAME%` to make a new directory
* Enter the command `%NAME%` to enter the newly made directory
* Enter the command `subl .`
* Make a new file 
* Copy the code

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver');

driver.get("https://carmudi.com.ph")

assert driver.page_source.find(" <  "u"\u20B1" "500,000 ")
assert driver.page_source.find("  "u"\u20B1" "500,000 -  "u"\u20B1" "1,000,000 ")
assert driver.page_source.find("  "u"\u20B1" "500,000 -  "u"\u20B1" "1,000,000 ")
assert driver.page_source.find("> "u"\u20B1""2,000,000 ")

print ('Successfully asserted')

```
* Paste the code in the newly made file
* Save the file and name it "%NAME%.py"
* Go back to the terminal
* Enter the command `python %NAME%.py`
