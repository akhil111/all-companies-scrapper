import os

import csv

from bs4 import BeautifulSoup
import requests

files=os.listdir('/Users/akhilmaddu/downloads')
#os.chdir('/Users/akhilmaddu/downloads')

for i in files:
    if i.endswith('.csv'):
        with open(i,'r') as csv_file:
            reader=csv.reader(csv_file)
            for row in reader:
#               content=list(row[i] for i in reader)
                print(row[2])
                page=requests.get('https://www.zaubacorp.com/company/{}/U72900DL2000PTC103639'.format(row[2]))        
                soup=BeautifulSoup(page.content, 'html.parser')
                email=soup.find_element_by_tag('div',class_="col-lg-6 col-md-6 col-sm-12 col-xs-12")
                print(email.get_text())


                        



