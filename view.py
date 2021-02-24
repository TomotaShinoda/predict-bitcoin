import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from assets.database import db_session
from assets.models import Data

# 外部のスタイルシートを取得
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# インスタンスを生成
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# DBからデータを取得
data = db_session.query(Data.date, Data.real_price, Data.pred_price).all()

# 取得したデータを項目ごとに分配
dates = []
real_prices = []
pred_prices = []

for _data in data:
    dates.append(_data.date)
    real_prices.append(_data.real_price)
    pred_prices.append(_data.pred_price)

# グラフのレイアウトを作成
layout = go.Layout(
    height=600,
    xaxis={
        "title":{
            "text":"日付"
        },
        "rangeslider":{"visible":True},
        'rangeselector':{
            'buttons':[
                {'label':'1週', 'step':'day', 'count':7},
                {'label':'1月', 'step':'month', 'count':1},
                {'label':'半年', 'step':'month', 'count':6},
                {'label':'1年', 'step':'year', 'count':1}
            ]
        }
    },
    yaxis={
        "title":{
            "text":"相場（ビットコイン対日本円）"
        }
    },
    margin=dict(l=300, r=300, t=50, b=100)
)

# 予測相場グラフの作成
pred_graph = go.Scatter(
    x=dates, 
    y=pred_prices,
    name='予測した価格'
)

# 実際の相場グラフの作成
real_graph = go.Scatter(
    x=dates, 
    y=real_prices,
    name='実際の価格'
)

# グラフとレイアウトの登録
fig = go.Figure(
    data=[real_graph, pred_graph],
    layout=layout
)

# グラフのコンポーネントを作成
graph = html.Div(
    children=[
        dcc.Graph(
            figure=fig
        )
    ]
)

# トップのコンポーネントを作成
top = html.H2(
    children='ビットコインの相場予測', 
    style={
        'textAlign':'center'
    }
)

# 相場表示のstyleを作成
div_style = {
    'width':'40%',
    'margin':'5%',
    'display':'inline-block',
    'textAlign':'center',
    'backgroundColor':'#DDFFFF'
}

# 実際相場を表示するコンポーネントを作成
real_price = html.Div(
    children=[
        html.H4(
            children='実際の今日の相場：￥%s'%real_prices[-2]
        ),
        html.H4(
            children=dates[-2]
        )
    ],
    style=div_style
)

# 予測相場を表示するコンポーネントを作成
pred_price = html.Div(
    children=[
        html.H4(
            children='予測した明日の相場：￥%s'%pred_prices[-1]   
        ),
        html.H4(
            children=dates[-1]
        )
    ],
    style=div_style
)

# 相場表示のコンポーネントを作成
view_price = html.Div([real_price,pred_price])

# レイアウトの作成
app.layout = html.Div(
    children=[
        top,
        view_price,
        graph
    ]
)

# アプリケーションを起動
if __name__ == '__main__':
    app.run_server(debug=True)
