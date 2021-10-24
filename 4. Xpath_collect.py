import requests
from lxml import etree, html
url = "https://hk.yahoo.com/"

res=requests.get(url)
#用lxml的html函式來處理內容格式

byte_data = res.content
source_code = html.fromstring(byte_data)
result = source_code.xpath('//*[@id="header-search-keywords"]/a[1]/text()')

print(result)