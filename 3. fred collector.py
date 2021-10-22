import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

# end date should be today, and the format should be YYYY-MM--DD
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
this_year = now.year
last_year = int(now.year) - 5

raw_start_date = datetime.datetime(last_year,month,day)
start_date = raw_start_date.strftime('%Y-%m-%d')
raw_end_date = datetime.datetime(this_year,month,day)
end_date= raw_end_date.strftime('%Y-%m-%d')

print(start_date)
print(end_date)

###to collect each ticker data
data = pd.read_csv("Fred.csv") #### you can add your ticker inside the csv
all_data = data.symbol.to_list()

###convert them to be csv
for fred_data in all_data:
    print(fred_data)
    df = web.DataReader(fred_data, 'fred', start_date, end_date)
    df.to_csv(f'{fred_data}.csv')
    print(df.head())
