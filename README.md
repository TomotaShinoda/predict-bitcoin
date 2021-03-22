# predict-bitcoin
ビットコインの相場を予測するWebアプリケーションです。  
URL：https://predict-bitcoin.herokuapp.com/  
  
LINE公式アカウントの追加はこちらです。  
https://lin.ee/4Kdebvv  

  
## 概要
近年ビットコインを用いた資産運用が注目を集めています。  
しかし、ビットコインを買うことに不安を感じている人が日本では多くいるのが現状です。  
この不安というのは未来のビットコインの相場が減少してしまうことへの懸念から生じています。  
この問題を解決するために、ビットコインの未来の相場を予測するwebアプリケーションを作成し、人々が安心してビットコインを買い、保有できるようにしたいです。  
予測する際の機械学習手法はLSTMを用いています。  
日本時間で09:00に定期実行するように設定してあり、このタイミングで翌日の相場を予測します。  
予測した結果をより簡単に、そしてより早くに知るために、LINEに通知してくれます。  
こちらよりLINE公式アカウントの追加が可能です。  
https://lin.ee/4Kdebvv  
  
    
## 実装機能・内容  
➀ビットコインの翌日相場を予測する機能  
 ⇒日本時間の 09:00 にビットコインの相場情報を取得し、翌日の相場を予測する機能です。  
    
➁可視化機能  
 ⇒過去２年分の相場情報と、毎日取得する相場情報を用いてチャートとして可視化する機能です。  
    
➂LINE公式アカウントによる通知機能  
 ⇒上記のURLよりLINE公式アカウントを友達追加することで、毎日 09:00 に当日の相場と翌日の相場予測結果を通知する機能です。
  
    
## 使用技術、開発環境
・Python 3.7.9  
・Dash 1.19.0  
・Flask 1.1.2  
・SQLite 3.33.0  
・SQLAlchemy 1.3.23  
・TensorFlow 1.15.3  
・Keras 2.2.4  
・Numpy 1.19.2  
・Plotly 4.14.3  
・Pandas 1.0.4  
・Requests 2.25.1  
・gunicorn 19.7.1  
・psycopg2 2.7.7  

・Coincheck API  
・Cryptowatch API  

・Heroku

＊ローカルで開発をしている際はAnacondaの仮想環境で開発をしておりました。  
  
## 今後の展望
・予測の精度を向上させるために異なる機械学習手法を用いたり、入力データを工夫する  
・翌日の予測だけでなく幅広い時間での予測を機能として追加する  
・相場の急な変化が起こった時にLINEに通知してくれる機能を追加する  
・デモトレードの機能を追加する  
・実際の取引を自動で行う自動売買botを作成する  
・他の仮想通貨や株価でも同様のことができるようにする  
  
## 参考文献  
・[Python Documentation](https://docs.python.org/ja/3.7/)  
・[Dash Documentation](https://dash.plotly.com/)  
・[Keras Documentation](https://keras.io/ja/)  
・[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/13/)  
・[LINE Messaging API Documentation](https://developers.line.biz/ja/docs/messaging-api/)  
・[Heroku Documentation](https://devcenter.heroku.com/categories/reference)  
・[Coincheck API Documentation](https://coincheck.com/ja/documents/exchange/api)  
・[HTMLクイックリファレンス](http://www.htmq.com/)
