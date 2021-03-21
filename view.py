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

# トップのコンポーネントを作成
top = html.H2(
    children='ビットコインの相場予測 （ BTC / JPY ）',
    style={
        'textAlign':'center',
        'margin':'3%'
    }
)

# 相場表示のstyleを作成
div_style = {
    'width':'40%',
    'margin':'3%',
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
            children='＊%s の相場'%dates[-2].strftime('%Y-%m-%d  %H:%M')
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
            children='＊%s の相場'%dates[-1].strftime('%Y-%m-%d  %H:%M')
        )
    ],
    style=div_style
)

# 相場表示のコンポーネントを作成
view_price = html.Div(
    children = [
        real_price,
        pred_price
    ],
    style = {
        'textAlign':'center'
    }
)

# グラフのレイアウトを作成
layout_graph = go.Layout(
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
    margin=dict(l=300, r=300, t=100, b=50)
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
    data=[real_graph,pred_graph],
    layout=layout_graph
)

# グラフのコンポーネントを作成
graph = html.Div(
    children=[
        dcc.Graph(
            figure=fig
        )
    ]
)

# LINE公式アカウントの説明を載せるコンポーネントを作成
line_top = html.H5(
    children = 'こちらのLINE公式アカウントを追加すると、毎日ビットコインの相場予測結果を通知してくれます！',
    style={
        'textAlign':'center',
        'margin':'2%'
    }
)

style_line = {
    'width':'35%',
    'display':'inline-block',
    'textAlign':'center',
    'verticalAlign':'middle'
}

# LINE公式アカウントのQRコードを載せるコンポーネントを作成
info_qr = html.Div(
    children=[
        html.Img(
            src = 'assets/line_qr.png'
        ),
    ],
    style=style_line
)

# LINE公式アカウントのリンクを載せるコンポーネントを作成
info_url = html.Div(
    children=[
        html.A(
            children = "こちらをクリックすると友達追加できます！",
            href = 'https://lin.ee/4Kdebvv',
            target = "_blank",
            style = {
                'fontSize':'15pt',
                'fontWeight':'bold'
            }
        )
    ],
    style=style_line
)

# アカウントのQRとリンクのコンポーネントをまとめる
line_account = html.Div([info_qr, info_url])

# LINEの情報をまとめる
line_info = html.Div(
    children=[
        line_top,
        line_account
    ],
    style = {
        'textAlign':'center',
        'margin':'5%'
    }
)

# レイアウトの作成
app.layout = html.Div(
    children=[
        top,
        view_price,
        graph,
        line_info
    ]
)

# アプリケーションを起動
if __name__ == '__main__':
    app.run_server(debug=True)
