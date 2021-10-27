import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#匯入CSV
df = pd.read_csv('avocado-updated-2020.csv')
#設定dash app
app = dash.Dash()
##################設定dash的layout(((((((((((((((((((((((((((收集VALUE)))))))))))))))))))))))))
app.layout = html.Div(children=[    ###引入html. 設定div(內裙有三個元素:H1, Dropdown, Graph)
    html.H1(children="Avocado Prices Dashboard"), #內裡會有H1
    dcc.Dropdown(id='geo-dropdown',   #引入dcc, 做一個dropdown menu),設定id
                 options=[{'label': i, 'value': i}
                           for i in df['geography'].unique()], #dropdown序碼
                 value="New York"), #第一個你會選到的
    dcc.Graph(id='price-graph') #圖片id
])

###################設定好callback function((((((((將VALUE傳入去FUNCTION,再由FUNCTION輸出FIGURE#################
#當INPUT一變, OUTPUT就會變(UPDATE)
@app.callback(     #decorator
    Output(component_id='price-graph', component_property='figure'),####output 連接 GRAPH介面
    Input(component_id='geo-dropdown', component_property='value') ###input dropdown介面

)
#真正FUNCTION, 傳召PLOTLY的圖

#由INPUT觸發
def update_graph(selected_geography): #定義輸入單位
    filtered_df = df[df['geography'] == selected_geography] #當被抽中就成為filter的variable
    line_fig = px.line(filtered_df,                         #這是plotly的code
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Price in {selected_geography}')

    return line_fig #會傳召到OUTPUT

if __name__=='__main__':
    app.run_server(debug=True)

