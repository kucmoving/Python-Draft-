import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

#collect the information from user
ticker_1 = input("plz enter 1st ticker?" "e.g.TSLA")
ticker_2 = input("plz enter 1st ticker?" "e.g.AAPL")
start_date = input("when do you want to start?" "e.g. 2020-1-1")
end_date = input("when do you want to close?" "e.g. 2020-7-1")

df_1 = web.DataReader(ticker_1, 'yahoo', start_date, end_date)
df_2 = web.DataReader(ticker_2, 'yahoo', start_date, end_date)

df_1.to_csv(f'{ticker_1}.csv')
df_2.to_csv(f'{ticker_2}.csv')

#check the data
print(df_1.head())
print(df_2.head())

#to plot separate charts
fig = plt.figure(figsize=[14,6])
ax1 = fig.add_subplot(121, ylabel =ticker_1)   ##121 1是1X1的高度, 2是代表有2個圖 , 1是代表第一個圖
df_1['Close'].plot(ax = ax1, color ='r', lw=2.) #can ask user which data do they want to show (open, high, close, volumne)
ax2 = fig.add_subplot(122, ylabel =ticker_2)
df_2['Close'].plot(ax = ax2, color ='b', lw=2.)

plt.show()

