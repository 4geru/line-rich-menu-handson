---
title: "リッチメニューAPIを動かす"
---

リポジトリを clone してきます

```shell
git clone git@github.com:4geru/line-rich-menu-handson.git
```

今回のハンズオンでは Ruby / Python / Node.js / Golang に対応しています。
お好きな環境をご利用ください。

### 必要パッケージのインストール

必要なライブラリをインスールします。

:::details Ruby
```shell
cd ruby
bundle install
```
:::

:::details Python
```shell
cd python
pipenv install
```
:::

:::details Node.js
```shell
cd node
npm install
```
:::

:::details Golang
```shell
cd golang
go get
```
:::

### 環境変数の反映

LINE Develpersの情報をもとに、 `LINE_CHANNEL_SECRET` と `CHANNEL_CHANNEL_TOKEN` を貼り付けます。

| 変数 | 書いてある場所 |
| :--- | :--- |
| LINE_CHANNEL_SECRET | チャンネル基本設定 > チャネルシークレット |
| CHANNEL_CHANNEL_TOKEN | Messaging API設定 > チャネルアクセストークン |

:::details Ruby
```ruby:app.rb
def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # 上書きする
      config.channel_token = "LINE_CHANNEL_TOKEN"   # 上書きする
    }
end
```
:::

:::details Python
```python:main.py
line_bot_api = LineBotApi('LINE_CHANNEL_TOKEN') # 上書きする
```
:::

:::details Node.js
```javascript:index.js
const config = {
  channelAccessToken: 'LINE_CHANNEL_TOKEN', // 上書きする
  channelSecret: 'LINE_CHANNEL_SECRET'      // 上書きする
};
```
:::

:::details Golang
```go:main.go
func main() {
	bot, err := linebot.New(
		"LINE_CHANNEL_SECRET",   // 上書きする
		"CHANNEL_CHANNEL_TOKEN", // 上書きする
	)
```
:::

### 実行する

リッチメニューを登録します

:::details Ruby
```shell
bundle exec ruby app.rb
```
:::

:::details Python
```shell
pipenv run python main.py
```
:::

:::details Node.js
```shell
node index.js
```
:::

:::details Golang
```shell
go run main.go rich_menu_object.go
```
:::
