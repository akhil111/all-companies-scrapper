
#built-in modules
import time
import re
import os

#third-party modules
import requests
import webbrowser
from  lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()



page=requests.get('https://data.gov.in/catalog/company-master-data')
soup = BeautifulSoup(page.content, 'html.parser')
webpage = html.fromstring(page.content)
akhil=webpage.xpath('//a/@href')


links_list=[]
links_list1=[]
sub_links=[]
full_links=[]

for i in akhil:
	if "download" in i:
	    links_list.append(i)
#	print(i)

for i in links_list:
	print(i)

for i in links_list:
	webbrowser.open(i)

#pulling internal links
def pulling_sublinks():
    for i in akhil:
    	if "page" in i:
    		sub_links.append(i)
    		print(i)

#building full URLS
def building_links():
	for i in sub_links:
		full_links.append("https://data.gov.in"+i)


pulling_sublinks()
building_links()

#pulling rest of csv files
for i in full_links:
    page=requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    webpage = html.fromstring(page.content)
    akhil=webpage.xpath('//a/@href')
    for i in akhil:
    	if "download" in i:
    		links_list1.append(i)
    		print(i)
    		webbrowser.open(i)





time.sleep(6)
driver.quit()




