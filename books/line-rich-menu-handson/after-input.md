---
title: "コードの解説"
---
# 解説
## リッチメニューを作成する
[APIドキュメント: リッチメニューを作成する](https://developers.line.biz/ja/reference/messaging-api/#create-rich-menu)
[APIドキュメント: リッチメニューオブジェクト](https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object)
リッチメニューオブジェクトの管理は、別のファイルでリッチメニューオブジェクトだけを返す関数を作っています。

:::details Ruby
リッチメニューオブジェクトは `./ruby/rich_menu_object.rb` で定義しています。

```ruby:app.rb
def create_rich_menu(rich_menu_object)
  client.create_rich_menu(rich_menu_object)
end
```
:::

:::details Python
リッチメニューオブジェクトは `./python/rich_menu_object.py` で定義しています。

```python:main.py
# アクションの登録
def create_action(action):
    if action['type'] == 'uri':
        return URIAction(type=action['type'], uri=action.get('uri'))
    else:
        return RichMenuSwitchAction(type=action['type'], rich_menu_alias_id=action.get('richMenuAliasId'), data=action.get('data'))

# リッチメニューを作成する
def create_rich_menus(rich_menu_object):
    areas = [
        RichMenuArea(
            bounds=RichMenuBounds(x=info['bounds']['x'], y=info['bounds']['y'], width=info['bounds']['width'], height=info['bounds']['height']),
            action=create_action(info['action'])
        ) for info in rich_menu_object['areas']
    ]

    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=rich_menu_object['size']['width'], height=rich_menu_object['size']['height']),
        selected=rich_menu_object['selected'],
        name=rich_menu_object['name'],
        chat_bar_text=rich_menu_object['name'],
        areas=areas
    )
    return line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
```
:::

:::details Node.js
リッチメニューオブジェクトは `./node/rich_menu_object.js` で定義しています。

```javascript:index.js
const createRichMenu = async (richMenuObject) => {
  return await client.createRichMenu(
    richMenuObject
  )
}
```
:::

:::details Golang
リッチメニューオブジェクトは `./golang/rich_menu_object.go` で定義しています。

```go:main.go
func createRichMenu(bot *linebot.Client, richMenu linebot.RichMenu) string {
	res, err := bot.CreateRichMenu(richMenu).Do()
	if err != nil {
		log.Fatal(err)
	}
	return res.RichMenuID
}
```
:::

## リッチメニューに画像をアップロードする
[APIドキュメント: リッチメニューの画像をアップロードする](https://developers.line.biz/ja/reference/messaging-api/#upload-rich-menu-image)
画像は `./public/` 配下に `richmenu-a.png`, `richmenu-b.png` を準備しています。

:::details Ruby
```ruby:app.rb
def set_rich_menu_image(rich_menu_id, rich_menu_image_path)
  client.create_rich_menu_image(rich_menu_id, File.open(rich_menu_image_path))
end
```
:::

:::details Python
```python:main.py
def set_rich_menu_image(rich_menu_id, rich_menu_image_path):
    with open(rich_menu_image_path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
```
:::

:::details Node.js
```javascript:index.js
const setRichMenuImage = async (richMenuId, path) => {
  const filepath = join(__dirname, path);
  const buffer = readFileSync(filepath);

  const res = await client.setRichMenuImage(richMenuId, buffer);
}
```
:::

:::details Golang
```go:main.go
func setRichMenuImage(bot *linebot.Client, richMenuId string, filePath string) {
	if _, err := bot.UploadRichMenuImage(richMenuId, filePath).Do(); err != nil {
		log.Fatal(err)
	}
}
```
:::

## リッチメニューエイリアスを作成する
[APIドキュメント: リッチメニューエイリアスを作成する](https://developers.line.biz/ja/reference/messaging-api/#create-rich-menu-alias)
aliasの設定をすることで、今回新たに追加された `richmenuswitch` アクションを使うことができます。

:::details Ruby
```ruby:app.rb
def create_rich_menu_alias(rich_menu_id, rich_menu_alias_id)
  client.set_rich_menus_alias(rich_menu_id, rich_menu_alias_id)
end
```
:::

:::details Python
```python:main.py
def set_rich_menus_alias(rich_menu_id, rich_menus_alias_id):
    alias = RichMenuAlias(
        rich_menu_alias_id=rich_menus_alias_id,
        rich_menu_id=rich_menu_id
    )
    line_bot_api.create_rich_menu_alias(alias)
```
:::

:::details Node.js
```javascript:index.js
const setRichMenuAlias = async (richMenuId, richMenuAliasId) => {
  return await client.createRichMenuAlias(richMenuId, richMenuAliasId)
}
```
:::

:::details Golang
```go:main.go
func setRichMenuAlias(bot *linebot.Client, richMenuId string, richMenuAliasID string) {
	if _, err := bot.CreateRichMenuAlias(richMenuAliasID, richMenuId).Do(); err != nil {
		log.Fatal(err)
	}
}
```
:::

## リッチメニューをデフォルトのリッチメニューにする
[APIドキュメント: デフォルトのリッチメニューを設定する](https://developers.line.biz/ja/reference/messaging-api/#set-default-rich-menu)
全ユーザーに対して、デフォルトで表示されるリッチメニューの設定をします

:::details Ruby
```ruby:app.rb
def set_default_rich_menu(rich_menu_id)
  client.set_default_rich_menu(rich_menu_id)
end
```
:::

:::details Python
```python:main.py
def set_default_rich_menu(rich_menu_id):
    line_bot_api.set_default_rich_menu(rich_menu_id)
```
:::

:::details Node.js
```javascript:index.js
const setDefaultRichMenu = async (richMenuId) => {
  return await client.setDefaultRichMenu(richMenuId)
}
```
:::

:::details Golang
```go:main.go
func setDefaultRichMenu(bot *linebot.Client, richMenuId string) {
	if _, err := bot.SetDefaultRichMenu(richMenuId).Do(); err != nil {
		log.Fatal(err)
	}
}
```
:::

# +α
## ユーザーとのリンク
## ユーザーと紐づいていることの確認
## ユーザーとのリンク解除

