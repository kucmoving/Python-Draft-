import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

##################################################################################################設定SELENIMU 及BROWSER 狀態################
options = webdriver.ChromeOptions()
#options.add_argument('headless')
browser = webdriver.Chrome("C:/Users/carro/Desktop/chromedriver.exe", options=options)
###################################################################################################執行bs4###################################
browser.get("https://ycharts.com/indicators/us_investor_sentiment_bearish")
soup = BeautifulSoup(browser.page_source, "html.parser")

#to search the tag and css control and look for the location
classname = soup.find_all("td", class_= "col-6")
print(classname[13])

#to clear the text with .text.strip()
classname = soup.find_all("td", class_= "col-6")[13].text.strip()
print(classname)

#檢視原始碼

