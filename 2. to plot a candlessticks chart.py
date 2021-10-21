import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import plotly.graph_objects as go

#collect the information from user
stock_code = input("plz enter your stock ticker?" "e.g.TSLA")
start_date = input("when do you want to start?" "e.g. 2020-1-1")
end_date = input("when do you want to close?" "e.g. 2020-7-1")

#receive data from yahoo and change to csv
df = web.DataReader(stock_code, 'yahoo', start_date, end_date)
df.to_csv(f'{stock_code}.csv')

#check the data
print(df.head())

#to plot the ma, but have to turn on juypter
df = pd.read_csv(f'{stock_code}.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'])])

fig.show()

#df['10'] = df['Close'].rolling(window=10).mean()
#df['50'] = df['Close'].rolling(window=50).mean()
#df[['Close', '10', '50']].plot(figsize=(14,6), grid=True)
#plt.show()

