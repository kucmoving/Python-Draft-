import plotly
import pandas
import pandas as pd
import plotly.express as px ###匯入畫圖插件

##Plotly github有dataset
df = pd.read_csv('DFF.csv') ###匯入該檔案CSV檔案
df.head()
##########1. 觀察數據
##########2. 思考要plot怎樣的圖
##########3. 畫圖加入相關coding


#############################A. 時間圖
#1. 線圖
fig = px.line(df, x='DATE', y="DFF")
fig.show()
#2. 棒形圖
fig = px.bar(df, x='DATE', y="DFF")
fig.show()
#3. 範圍圖
fig = px.area(df, x='DATE', y="DFF")
fig.show()

##############################B. 分佈圖
#1. 點陣
fig = px.scatter(df, x='DATE', y="DFF")
fig.show()
#2. HISTOGRAM
fig = px.histogram(df, x='DATE', y="DFF", histfunc="sum", color="smoker")

#############################C. 多線圖
fig = px.line(title='全班同學的國文英文數學分數')
fig.add_scatter(x=df['姓名'], y=df['英文'],name='英文', showlegend = True)
fig.add_scatter(x=df['姓名'], y=df['數學'],name='數學', showlegend = True)
fig.show()
