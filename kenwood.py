import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from config import TELEGRAM_API_SEND_MSG
# Get updates: 
CHAT_ID = 403219767

def sendData(price, item, URL):

    data ={
        'chat_id' : CHAT_ID,
        'text' :  f'[{item}]({URL})\n {price}',
        'parse_mode': 'Markdown'
    }
    print(data)
    r_send=requests.post(TELEGRAM_API_SEND_MSG, data=data)

def get_digits(text):
    return re.sub('\D','',text)

# Not all website works
URL='https://www.kenwoodworld.com/uk/products/blenders/hand-mixers/handmix-lite-hmp30a0wh-0w22210012'
r=requests.get(URL)
soup=BeautifulSoup(r.text,'html.parser')
# 
price=soup.find('span',{'itemprop':'price'}).get_text(); 
item=soup.find('h1',{'itemprop':'name'}).get_text().strip(); 

if int(get_digits(price))<2498:
    sendData(price,item,URL)

#2 Warren Bluetooth Speaker
URL='https://www.zalora.sg/jbl-jbl-flip-3-stealth-edition-ipx7-waterproof-portable-bluetooth-speaker-black-1377916.html' 
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(URL)
soup=BeautifulSoup(driver.page_source,'html.parser')
#
price=soup.find('span',{'id':'js-detail_specialPrice_with_specificSize'}).get_text(); 
item=soup.find('div',{'class':'product__title fsm'}).get_text().strip(); 

if int(get_digits(price))<8900:
    sendData(price,item,URL)
driver.quit()
#3
URL='https://www.cultbeauty.co.uk/hourglass-ambient-lighting-blush-travel-size.html?variant_id=17122' 
r=requests.get(URL)
soup=BeautifulSoup(r.text,'html.parser')
#
price=soup.find('span',{'class':'productPrice js-product-price'}).get_text(); 
item=soup.find('div',{'class':'productBrandTitle'}).get_text().strip(); 

if int(get_digits(price))<2400:
    sendData(price,item,URL)
