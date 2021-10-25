########1.	Network> preview > click the tag (stack and …)> 確定該DATA相似
########到回HRADER GENERAL找網址, 再到request payload(是附加資訊要求)
########按view source, 注意有沒有show more, 全部盡取
#########Request header> user agenet一定要copy, / content type 也是
##https://www.youtube.com/watch?v=DSjVHqdbkBw
#https://codebeautify.org/python-formatter-beautifier
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json

url = "https://scanner.tradingview.com/cfd/scan"

headers = {
    'Content-type': "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

requests_data = {"symbols":{"tickers":["TVC:NDX"],"query":{"types":[]}},"columns":["Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX+DI","ADX-DI","ADX+DI[1]","ADX-DI[1]","AO","AO[1]","AO[2]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","EMA10","close","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1"]

}

r = requests.get(url, headers=headers, data=json.dumps(requests_data)).json()

data = json.dumps(r, indent=4)
data = json.loads(data)   ####將散亂的json 整合成真的json
print(data['data'][0]['d'][3])
