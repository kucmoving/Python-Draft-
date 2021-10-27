##DASH + PLOT ###is brothers==>interactive dashboard
#1)layout:how to display on the app
#2)callback:function

##have to use jupter with plotly

#1. 進行匯入
import pandas as pd
import plotly.express as px

#2. 匯入數據
df = pd.read_csv('avocado-updated-2020.csv')
df.info()

#3. 處理DATA
print(df['type'].value_counts(dropna=False)) ##不計算NA
print(df['geography'].value_counts(dropna=False)) ##不計算NA


msk = df['geography'] == 'Los Angeles' ##另起一個COLUMN
px.line(df[msk], x='date', y='average_price', color='type') #再PLOT出



#####dash-->have to use pycharm