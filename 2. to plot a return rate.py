import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import numpy as np

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

#to plot a combine chart
stock = pd.DataFrame({ticker_1: df_1['Close'],    ####to combine in one chart
                      ticker_2: df_2['Close']})

#to display a return rate
stock_return = stock.apply(lambda x: x / x[0])
print(stock_return.head())
stock_return.plot(figsize=(14,6), grid = True)

plt.show()

