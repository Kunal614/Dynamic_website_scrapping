import requests
from bs4 import BeautifulSoup


from selenium import webdriver
import time
import pandas as pd


import csv
driver = webdriver.Firefox()


url =("https://redef.com/source/5b4f57e380fbaa7507626ecb")

driver.get(url)





cnt = 0

check = {cnt:True}

while check[cnt] == True:
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html , features='lxml')
    data = soup.find_all("a" , class_="js-article-count-check")
    print(len(data))
    cnt = len(data)
    try:
        if check[cnt] == True:
            break
    except:
        check[cnt]=True      

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    



driver.close()
list1 = ["Title"]
list2 = ["Link"]

for news in data:
    list1.append(news['title'])
    list2.append("https://redef.com"+news['href'])


print(len(list1) , len(list2))

with open('test.csv' , 'w') as f:
    writer  = csv.writer(f , delimiter='\t')
    writer.writerows(zip(list1, list2))

