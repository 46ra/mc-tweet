# mc-tweet

## 概要
マルコフ連鎖を用いて自分のtweetから文を生成したり、それをtweetしたりできます。

## 使用方法
- このrepoを適当なところにcloneします。
- 自分の全tweet履歴をdownloadします（[参考](https://help.twitter.com/ja/managing-your-account/how-to-download-your-twitter-archive)）。
- downloadしたdataの中から`tweets.csv`を取り出してcloneしたrepoに直下に置きます（`mc-tweet/tweets.csv`）。
- `prepare.py`を実行します。

この後、

- `utter.py`を実行するとcommand lineに生成した文章を表示します。

また、

- https://apps.twitter.com/ でapplication登録を行い次の4つを取得します。
  - consumer key 
  - consumer secret
  - access token
  - access token secret
- `mc-tweet/tokens.txt`を作成し、4つを改行区切りで保存します。
- `tweet.py`を実行すると`utter.py`で文を生成しtweetします。
