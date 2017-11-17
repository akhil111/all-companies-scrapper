

#built-in modules
import time
import re

#third-party modules
import requests
import webbrowser
from  lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



 



driver = webdriver.Firefox()
driver.get("https://data.gov.in/catalog/company-master-data")


page=requests.get('https://data.gov.in/catalog/company-master-data')
soup = BeautifulSoup(page.content, 'html.parser')



webpage = html.fromstring(page.content)

akhil=webpage.xpath('//a/@href')

links_list=[]

for i in akhil:
	if "download" in i:
	    links_list.append(i)
#	print(i)

for i in links_list:
	print(i)

for i in links_list:
	webbrowser.open(i)



time.sleep(6)
driver.quit()



