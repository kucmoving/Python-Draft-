import pandas_datareader.data as web
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sn
#setting the time

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
this_year = now.year
last_year = int(now.year) - 1

raw_start_date = datetime.datetime(last_year,month,day)
start_date = raw_start_date.strftime('%Y-%m-%d')
raw_end_date = datetime.datetime(this_year,month,day)
end_date= raw_end_date.strftime('%Y-%m-%d')

#to ask which stocks should be downloaded
stock = input("please enter the stock you want to compare. e.g.'AAPL AMZN GOOG FB TSLA'")
stock_list = list(stock.split())
stock_num = len(stock_list)
portfolio = yf.download(stock_list, start_date, end_date)

#to plot
close=portfolio['Close']
portfolio["Close"].pct_change()
portfolio["Close"].pct_change().corr()

corrMatrix = portfolio["Close"].pct_change().corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()