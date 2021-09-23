---
title: "リッチメニューAPIを動かす"
---

LINE 公式が公開している[サンプル](https://developers.line.biz/ja/docs/messaging-api/using-rich-menus/#switching-between-multiple-rich-menus)を試していきます。
今回のハンズオンでは Ruby / Python / Node.js / Golang に対応しています。
まずは、今回使うリポジトリを clone してきます。

```shell
git clone git@github.com:4geru/line-rich-menu-handson.git
```

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
`ruby/app.rb` を開いて、`LINE_CHANNEL_SECRET` と `CHANNEL_CHANNEL_TOKEN` を上書きします。

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
`python/main.py` を開いて、`CHANNEL_CHANNEL_TOKEN` を上書きします。

```python:main.py
line_bot_api = LineBotApi('LINE_CHANNEL_TOKEN') # 上書きする
```
:::

:::details Node.js
`javascript/index.js` を開いて、`LINE_CHANNEL_SECRET` と `CHANNEL_CHANNEL_TOKEN` を上書きします。
```javascript:index.js
const config = {
  channelAccessToken: 'LINE_CHANNEL_TOKEN', // 上書きする
  channelSecret: 'LINE_CHANNEL_SECRET'      // 上書きする
};
```
:::

:::details Golang
`go/main.go` を開いて、`LINE_CHANNEL_SECRET` と `CHANNEL_CHANNEL_TOKEN` を上書きします。

```go:main.go
func main() {
	bot, err := linebot.New(
		"LINE_CHANNEL_SECRET",   // 上書きする
		"CHANNEL_CHANNEL_TOKEN", // 上書きする
	)
```
:::

### コードの実行

スクリプトを実行して、リッチメニューを登録します

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
