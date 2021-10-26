###http://liyangbit.com/pythonvisualization/Plotly-Express-introduction-cn/


###########df參數##################
#1. 指定時間df
df2007 = df.query('year == 2007')

############畫線參數###############
px.colors.qualitative.swatches()
px.colors.sequential.swatches()
color="continent", "smoker", "species"
size="pop"
size_max=60
title="chinese"
line_color="red"
############layout參數#############
#1. 時間軸
fig.update_xaxes(rangeslider_visible=True)
#2. 時間軸標記
fig.update_xaxes(
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


