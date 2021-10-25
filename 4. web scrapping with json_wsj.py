#i spend half day to find a method to pick data from WSJ. 24/12/2021
#it seems that only json and rewrite xpath works
#Step 1. to search the json from WSJ https://www.wsj.com/market-data/stocks/us
#right click > inspect > network > XHR > choose the one with relative data
#reference:https://lufor129.medium.com/%E6%89%8B%E6%8A%8A%E6%89%8B%E5%AF%AB%E5%80%8B%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-%E4%B8%80-xpath-518553fd676d
#referene:https://stackoverflow.com/questions/60606633/scraping-wsj-com
#https://www.wsj.com/market-data/stocks/us?id={"application":"WSJ","marketsDiaryType":"overview"}&type=mdc_marketsdiary
#https://www.learncodewithmike.com/2020/10/scraping-ajax-websites-using-python.html

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json

url = "https://www.wsj.com/market-data/stocks"
params = {
    'id': '{"application":"WSJ","marketsDiaryType":"overview"}',
    'type': 'mdc_marketsdiary'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
}
r = requests.get(url, params=params, headers=headers).json()

data = json.dumps(r, indent=4)
data = json.loads(data)    ####將散亂的json 整合成真的json
print(data["data"]["instrumentSets"][0]['instruments'][0]['NASDAQ']) #advancing nasdaq
print(data["data"]["instrumentSets"][0]['instruments'][0]['NYSE'])   #advancing nyse
print(data["data"]["instrumentSets"][0]['instruments'][1]['NASDAQ']) #decline nasdaq
print(data["data"]["instrumentSets"][0]['instruments'][1]['NYSE'])   #decline nyse

