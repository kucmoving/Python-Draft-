import plotly
import pandas
import pandas as pd
import plotly.express as px ###匯入畫圖插件

#DFF
df_dff = pd.read_csv('DFF.csv') ###匯入該檔案CSV檔案
fig_dff = px.line(df_dff, x='DATE', y="DFF", title="Federal Funds Effective Rate")
fig_dff.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_dff.show()

#WALCL
df_walcl = pd.read_csv('WALCL.csv') ###匯入該檔案CSV檔案
fig_walcl = px.area(df_walcl, x='DATE', y="WALCL", title="Assets: Total Assets: Total Assets (Less Eliminations from Consolidation)")
fig_walcl.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_walcl.show()


#T10Y3M
df_t10y3m = pd.read_csv('T10Y3M.csv') ###匯入該檔案CSV檔案
fig_t10y3m = px.area(df_t10y3m, x='DATE', y="T10Y3M", title=" 10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity")
fig_t10y3m.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_t10y3m.show()

#T10Y2Y
df_t10y2y = pd.read_csv('T10Y2Y.csv') ###匯入該檔案CSV檔案
fig_t10y2y = px.area(df_t10y2y, x='DATE', y="T10Y2Y", title="10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity")
fig_t10y2y.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_t10y2y.show()


#A822RE1Q156NBEA
df_a8 = pd.read_csv('A822RE1Q156NBEA.csv') ###匯入該檔案CSV檔案
fig_a8 = px.bar(df_a8, x='DATE', y="A822RE1Q156NBEA", title="Shares of gross domestic product: Government consumption expenditures and gross investment")
fig_a8.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_a8.show()

#UNRATE
df_unrate = pd.read_csv('UNRATE.csv') ###匯入該檔案CSV檔案
fig_unrate = px.bar(df_unrate, x='DATE', y="UNRATE", title="Unemployment Rate")
fig_unrate.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig_unrate.show()