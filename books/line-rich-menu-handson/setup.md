---
title: "LINE Botの準備"
---

# LINE Botの登録

[LINE Developers](https://developers.line.biz/console/) からLINEの設定をしていきます

## 初回利用の方は新規プロバイダーの登録をしてください
:::details LINE Developerの登録(初回利用の方のみ)
[#Messaging APIを始めよう](https://developers.line.biz/ja/docs/messaging-api/getting-started/) を参考に 3. まで進めてください。

1. LINE Developersコンソールにログインする
2. 開発者として登録する（初回ログイン時のみ）
3. 新規プロバイダーを作成する
:::

## LINE Botの作成

Messaging APIでアカウントを作成していきます。
![](/images/books/line-rich-menu-handson/setup/create-line-bot-channel.png)

```text
チャンネル名: リッチメニュー切り替えアプリ
チャネル説明: リッチメニューを切り替えるアプリです
大業種: 個人
小業種: 個人（その他）
```

規約にチェックを入れて、次に進みます。
同意の確認画面が出ますが、そのまま進んでください。

## 環境変数の準備
### `LINE_CHANNEL_SECRET`

botの詳細画面から `チャネル基本設定 > チャネルシークレット` から `LINE_CHANNEL_SECRET` をメモします。
![](/images/books/line-rich-menu-handson/setup/channel-secret.png)

### `LINE_CHANNEL_TOKEN`

botの詳細画面から `Messaging API設定 > チャネルアクセストークン（長期）` 発行を押します。
`LINE_CHANNEL_TOKEN` が作成されるので、メモします。
![](/images/books/line-rich-menu-handson/setup/channel-access-token.png)

## 友達追加

botの詳細画面から `Messaging API設定 > ボット情報` からどちらかでbotを追加します。
- `ボットのベーシックID` から友達追加する
- `QRコード` から友達追加をする
