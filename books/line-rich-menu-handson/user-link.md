---
title: "おまけ：ユーザーリンク"
---

# ユーザーリンクについて
今回のハンズオンでは、 `リッチメニュー切替アクション` について解説しました。
今まで通り Messaging API からの切り替えもできます。おまけとして、ユーザーリンクについてもまとめます。

## user_id について

[LINE Developers](https://developers.line.biz/) の botの詳細画面から `チャネル基本設定 > あなたのユーザーID` をメモします。

## 前準備
それぞれの環境で、ユーザーリンクをテストするスクリプトを実行します。
今登録されているリッチメニューが表示されるので、メモします。
各言語のディレクトリに user_link.xx というファイルがあります。
ユーザーリンクについてはコメントアウトされています。
コメントアウトを外して、挙動の確認をしてみましょう。

:::details Ruby
```shell
bundle exec ruby user_link.rb
```
:::

:::details Python
```shell
pipenv run python user_link.py
```
:::

:::details Node.js
```shell
node user_link.js
```
:::

:::details Golang
```shell
make test
```
:::


## ユーザーとのリンク/リンク解除
[リッチメニューとユーザーをリンクする](https://developers.line.biz/ja/reference/messaging-api/#link-rich-menu-to-user)
[リッチメニューとユーザーのリンクを解除する](https://developers.line.biz/ja/reference/messaging-api/#unlink-rich-menu-from-user)

::: details Ruby
```ruby:user_link.rb
client.link_user_rich_menu(user_id, richmenu_id)
client.unlink_user_rich_menu(user_id)
```
:::

:::details Python
```python:user_link.py
line_bot_api.link_rich_menu_to_user(user_id, richmenu_id)
line_bot_api.unlink_rich_menu_from_user(user_id)
```
:::

:::details Node.js
```javascript:user_link.js
client.linkRichMenuToUser(userId, richmenuId)
client.unlinkRichMenuFromUser(userId)
```
:::

:::details Golang
```go:user_link.go
if res, _ := bot.LinkUserRichMenu(userId, richmenuId).Do(); res != nil {
  log.Printf("Response %v;", res)
}

if res, _ := bot.UnlinkUserRichMenu(userId).Do(); res != nil {
  log.Printf("Response %v;", res)
}
```
:::

## ユーザーと紐づいていることの確認
[ユーザーのリッチメニューのIDを取得する](https://developers.line.biz/ja/reference/messaging-api/#get-rich-menu-id-of-user)

::: details Ruby
```ruby:user_link.rb
p client.get_user_rich_menu(user_id)
```
:::

:::details Python
```python:user_link.py
print(line_bot_api.get_rich_menu_id_of_user(user_id))
```
:::

:::details Node.js
```javascript:user_link.js
client.getRichMenuIdOfUser(userId).then((r) => {
  console.log(r)
})
```
:::

:::details Golang
```go:user_link.go
if res, _ := bot.GetUserRichMenu(userId).Do(); res != nil {
  log.Printf("Response %v;", res)
}
```
:::

## ユーザーとの一括リンク/リンク解除
[リッチメニューと複数のユーザーをリンクする](https://developers.line.biz/ja/reference/messaging-api/#link-rich-menu-to-users)
[複数のユーザーのリッチメニューのリンクを解除する](https://developers.line.biz/ja/reference/messaging-api/#unlink-rich-menu-from-users)

::: details Ruby
```ruby:user_link.rb
client.bulk_link_rich_menus([user_id], richmenu_id)
client.bulk_unlink_rich_menus([user_id])
```
:::

:::details Python
```python:user_link.py
line_bot_api.link_rich_menu_to_users([user_id], richmenu_id)
line_bot_api.unlink_rich_menu_from_users([user_id])
```
:::

:::details Node.js
```javascript:user_link.js
client.linkRichMenuToMultipleUsers(richmenuId, [userId])
client.unlinkRichMenusFromMultipleUsers([userId])
```
:::

:::details Golang
```go:user_link.go
if res, _ := bot.BulkLinkRichMenu(richmenuId, userId, userId).Do(); res != nil {
  log.Printf("Response %v;", res)
}

if res, _ := bot.BulkUnlinkRichMenu(userId, userId).Do(); res != nil {
  log.Printf("Response %v;", res)
}
```
:::