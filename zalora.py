import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

# Get updates: 

CHAT_ID = 403219767
#CHAT_ID = 85047147

TOKEN = '1308198218:AAGfsSL-ebgWjRPr3_l0yvf1mikUN1izet8'
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
print(TELEGRAM_API_SEND_MSG)
    # Not all website works with requests.
URL='https://www.zalora.sg/jbl-jbl-flip-3-stealth-edition-ipx7-waterproof-portable-bluetooth-speaker-black-1377916.html' 

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(URL)
print(driver.page_source)
soup=BeautifulSoup(driver.page_source,'html.parser')


price=soup.find('span',{'id':'js-detail_specialPrice_with_specificSize'}).get_text(); 
item=soup.find('div',{'class':'product__title fsm'}).get_text().strip(); 
print(item)

if int(price)<= 89:
    print(price) 

data ={
    'chat_id' : CHAT_ID,
    'text' :  f'[{item}]({URL})\n {price}',
    'parse_mode': 'Markdown'
}

r_send=requests.post(TELEGRAM_API_SEND_MSG, data=data)
driver.quit()