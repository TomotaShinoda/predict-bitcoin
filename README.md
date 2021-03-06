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
予測した結果をより簡単に、そしてより早くに知るために、LINEに通知してくれます。  
こちらよりLINE公式アカウントの追加が可能です。  
https://lin.ee/4Kdebvv  
  
    
## 実装機能・内容  
➀ビットコインの翌日相場を予測する機能  
 ⇒日本時間の 09:00 にビットコインの相場情報を取得し、翌日の相場を予測する機能です。  
    
➁可視化機能、ズーム機能  
 ⇒過去２年分の相場情報と、毎日取得する相場情報を用いてチャートとして可視化する機能です。チャートは拡大・縮小できます。  
    
➂LINE公式アカウントによる通知機能  
 ⇒上記のURLよりLINE公式アカウントを友達追加することで、毎日 09:00 に当日の相場と翌日の相場予測結果を通知する機能です。  
 
 
## 使い方  
### チャートの拡大・縮小  
![チャート説明図](https://user-images.githubusercontent.com/74633209/112714922-28226400-8f20-11eb-8c54-4548776a8337.png)  
➀のスライダと➁のボタンでは表示する期間を自由に変更できます。  
➂の名称をクリックすると表示するチャートを変更できます。  
  
### LINE公式アカウントによる通知  
![スクリーンショット (50)](https://user-images.githubusercontent.com/74633209/112715120-f4e0d480-8f21-11eb-8e27-50a7afa079b8.png)  
LINE公式アカウントを友達追加すると、毎日09:00に写真のようなメッセージが配信されます。  
  
  
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
・gunicorn 19.7.1 (WSGIサーバー)   
・psycopg2 2.7.7  

・Coincheck API  
・Cryptowatch API  
・LINE Messaging API

・Heroku（インフラ）

＊ローカルではWindows10でAnacondaの仮想環境を作成して開発をしておりました。  
  
## 課題と今後の展望
・予測の精度を向上させるために異なる機械学習手法を用いたり、入力データを工夫する  
・翌日の予測だけでなく幅広い時間での予測を機能として追加する  
・相場の急な変化が起こった時にLINEに通知してくれる機能を追加する  
・デモトレードの機能を追加する  
・実際の取引を自動で行う自動売買botを作成する  
・他の仮想通貨や株価でも同様のことができるようにする  
   
## 自己評価、感想  
ビットコインの相場を予測する難しさを改めて感じました。ビットコインの相場は国や企業の動き、政治や経済のような様々な要素により決定されるので、入力する説明変数を増やしてより高確率で当たるモデルを作成していきたいです。  
webアプリケーションの作成においてはHerokuでデプロイする際に苦労しました。TensorFlow 2.x のバージョンでは容量が重く、slugサイズが500MBをオーバーしてしまいました。これを改善するため、TensorFlorのバージョンを1.15.3にすることで軽量化に成功し、Herokuで公開することができました。  
webアプリケーションとLINEを連携させた点は良い工夫だと感じます。APIを用いることで比較的簡単に実現したい機能を実装でき感動しました。  
現状ではアプリケーションの機能が少ないので、今後機能を増やしていきたいです。  

  
## 参考文献  
・[Python Documentation](https://docs.python.org/ja/3.7/)  
・[Dash Documentation](https://dash.plotly.com/)  
・[Keras Documentation](https://keras.io/ja/)  
・[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/13/)  
・[LINE Messaging API Documentation](https://developers.line.biz/ja/docs/messaging-api/)  
・[Heroku Documentation](https://devcenter.heroku.com/categories/reference)  
・[Coincheck API Documentation](https://coincheck.com/ja/documents/exchange/api)  
・[Cryptowatch API で過去の相場データを取得](http://liibercraft.com/archives/30)  
・[HTMLクイックリファレンス](http://www.htmq.com/)  
・[Python インタラクティブ・データビジュアライゼーション 入門](https://www.asakura.co.jp/books/isbn/978-4-254-12258-9/)
