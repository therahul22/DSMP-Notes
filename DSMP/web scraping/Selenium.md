It can interact with dynamic websites

- install selenium
- install chromedriver
- opening a webpage - starter code


# Getting Data

from selenium import webdriver
from selenium. webdriver chrome service import Service

s = Service("C:/Users/Rahul/Desktop/chromedriver.exe")

- created a driver object
    driver = webdriver.Chrome(service = s)

- loading a webpage
    driver.get('web link')

- Finding an element on screen
    driver.find_element(by=By.XPATH, value='xpath')

- we can execute JS using driver
    driver.execute_script(' ')

- Fetching html code
      htmlfile = driver.page_source
      with open('file.html', 'w', encoding='utf-8') as f:
        f.write(htmlfile)

# Working with file - Scraping

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmlfile, lxml)

soup.find_all('div', {'class': 'product-page phones'})

- make a list, append info into list.
- make df using list