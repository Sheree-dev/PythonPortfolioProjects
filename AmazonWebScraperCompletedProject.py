#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import libraries 
import requests
from bs4 import BeautifulSoup
import time
import datetime

import smtplib


# In[3]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text() 
div = soup2.find('div', class_= 'a-section a-spacing-none aok-align-center aok-relative')
price = div.span.text

print(title)
print (price)


# In[4]:


# Clean up the data a little bit

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[7]:


#Import Date time for date obj
import datetime
today = datetime.date.today()


# In[9]:


# Import csv
# Create CSV file to store data in data set
# and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
# Check if file was created


# In[13]:


# Write all code into one funtion for reusability

def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    
    div = soup2.find('div', class_= 'a-section a-spacing-none aok-align-center aok-relative')
    price = div.span.text

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
 
    


# In[14]:


# Check file using pandas

import pandas as pd

df = pd.read_csv(r'C:\Users\Sheree\AmazonWebScraperDataset.csv')

print(df)


# In[15]:


# Apend data to the csv file

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


# Import Time library to create a timer object
# Runs check_price function every 24 hours to input data into the CSV file

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


# Check file using pandas

import pandas as pd

df = pd.read_csv(r'C:\Users\Sheree\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:




