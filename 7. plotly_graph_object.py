import plotly
import pandas
import numpy
import pandas as pd
import plotly.graph_objects as go ###匯入畫圖插件

##Plotly github有dataset
data = pd.read_csv('symbol.csv') ###匯入CSV檔案
data.head()

##########1. 觀察數據
##########2. 思考要plot怎樣的圖
##########3. 畫圖加入相關coding
######################單數據線###########################
data = pd.read_csv('DFF.csv') ###匯入該檔案CSV檔案
data.head()

data['DFF'], data['DATE']  ###左面有號碼順序是正常的

line = go.Scatter(x=data['DATE'], y=data['DFF']) #進行畫線, 定好X,Y / 再定義為X
fig = go.Figure(line) #將LINE放在圖內
fig.show()

###download, autoscale


######################雙數據線###########################
data = pd.read_csv('DFF.csv') ###匯入該檔案CSV檔案
data.head()

line1 = go.Scatter(x=data['DATE'], y=data['DFF'], name='Auckland') #設定好兩條線並進行命名
line2 = go.Scatter(x=data['DATE'], y=data['ABC'], name='Wellington') #設定好兩條線並進行命名
fig = go.Figure(line1, line2) #將LINE放在圖內

fig.update_layout(                  #設定X Y軸標題
    title = "New Zealand Weather",
    xaxis_title = "Date",
    yaxis_title = "Weather"
)

fig.show()

#################畫出棒形圖
data = pd.read_csv('DFF.csv') ###匯入該檔案CSV檔案
data.head()
###################指定特定日期##########################
data_2018 = data[(data['DATE'] >= '2018-01') & (data['DATE'] < '2019-01')]
data_2018

bar1 = go.Bar(x=data_2018['DATE'], y=data_2018['DFF'],##利用go.Bar畫棒, 並定義為bar
              text = data_2018['DFF'], textposition='outside') #並將數值放在bar的上方

fig = go.Figure(bar1) #將棒棒放入圖
fig.show()#展示圖片
##################雙棒形圖######################
bar1 = go.Bar(x=data_2018['DATE'], y=data_2018['DFF'],##利用go.Bar畫棒, 並定義為bar
              text = data_2018['DFF'], textposition='outside', name="auckland") #並將數值放在bar的上方
bar2 = go.Bar(x=data_2018['DATE'], y=data_2018['ABC'],##利用go.Bar畫棒, 並定義為bar
              text = data_2018['ABC'], textposition='outside', name="wellington") #並將數值放在bar的上方
fig = go.Figure(bar1, bar2) #將棒棒放入圖
fig.show()#展示圖片
#################分佈統計圖################
hist = go.Histogram(x = data['DFF'], xbins={'size':10}) #分佈一格是10
fig = go.Figure(hist)
fig.update_layout(bargap=0.1) ##加入柱間距離
fig.show()
########################################
area = go.Area(x = data['DFF'], facet_col_wrap=2) #分佈一格是10
fig = go.Figure(area)
fig.show()