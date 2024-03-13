from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import undetected_chromedriver as uc

driver=uc.Chrome()
driver.get('https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market')
driver.implicitly_wait(20)
driver.maximize_window()

r = 1
templist = []


while(1):
    try:
        name = driver.find_element(By.XPATH, '//*[@id="livePreTable"]/tbody/tr['+str(r)+']/td[2]/a').text
        lastPrice = driver.find_element(By.XPATH, '//*[@id="livePreTable"]/tbody/tr['+str(r)+']/td[7]').text
        Table_dict = {
        'Name': name,
        'LastPrice': lastPrice
        }
        templist.append(Table_dict)
        df = pd.DataFrame(templist)
        r += 1
    except NoSuchElementException:
        break

df.to_csv('table.csv')
driver.close()