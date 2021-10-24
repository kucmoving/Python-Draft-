from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.moneydj.com/ETF/X/Basic/Basic0007.xdjhtm?etfid=TAN")
yc_web_page = response.text ####網址可TEXT 便是HTML

#做湯,creating object
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="div", class_="eTitle") #找出標題HTML

print(article_tag.getText())


