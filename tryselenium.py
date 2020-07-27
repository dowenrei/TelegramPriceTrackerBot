from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
url = "https://www.zalora.sg/jbl-jbl-flip-3-stealth-edition-ipx7-waterproof-portable-bluetooth-speaker-black-1377916.html"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
print(soup.prettify())
