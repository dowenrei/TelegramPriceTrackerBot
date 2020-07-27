import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

# Get updates: 


CHAT_ID = 403219767

TOKEN = '1308198218:AAGfsSL-ebgWjRPr3_l0yvf1mikUN1izet8'
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
print(TELEGRAM_API_SEND_MSG)
    # Not all website works with requests.
URL='https://www.cultbeauty.co.uk/hourglass-ambient-lighting-blush-travel-size.html?variant_id=17122' 


r=requests.get(URL)
soup=BeautifulSoup(r.text,'html.parser')

price=soup.find('span',{'class':'productPrice js-product-price'}).get_text(); 
item=soup.find('div',{'class':'productBrandTitle'}).get_text().strip(); 

data ={
    'chat_id' : CHAT_ID,
    'text' :  f'[{item}]({URL})\n {price}',
    'parse_mode': 'Markdown'
}

print(data)
r_send=requests.post(TELEGRAM_API_SEND_MSG, data=data)
#driver.quit()






