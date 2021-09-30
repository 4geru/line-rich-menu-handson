---
title: "リッチメニューオブジェクトについて解説"
---

リッチメニューを構成するオブジェクトについて詳しく解説します。
[リッチメニューオブジェクト](https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object)

リッチオブジェクトの例
```json
{
  "size": {
    "width": 2500, // 800px < width < 2500px
    "height": 1686 // 250px < height < 1686
  },
  "selected": false,
  "name": "Nice richmenu", // 開発用のリッチメニュー名
  "chatBarText": "Tap to open", // トークルームメニューに表示される部分
  "areas": [ // タップエリア
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 1686
      },
      "action": {
        "type": "postback",
        "data": "action=buy&itemid=123"
      }
    }
  ]
}
```

# selected
bot 画面に遷移したときにデフォルトの表示するか、しないかの設定です。
今回のハンズオンでは、デフォルト表示しない設定でしたが、 デフォルト表示する設定の方が多いようです。

# chatBarText

赤枠の部分に表示せるメッセージです。最大14文字登録できます。
`タップしてキーボードを表示`, `おすすめを表示させる`, `9/30までWebクーポン` など様々な活用方法があります。

![](/images/books/line-rich-menu-handson/rich-menu-option/chat-bar-area.jpg =250x)

# areas
リッチメニューオブジェクトのタッチできるエリアです。タッチする座標と発火させるアクションを指定します。最大20オブジェクト登録できます。

[テンプレートメッセージ](https://developers.line.biz/ja/docs/messaging-api/message-types/#template-messages)、[Flex Message](https://developers.line.biz/ja/docs/messaging-api/message-types/#flex-messages)、[クイックリプライ](https://developers.line.biz/ja/docs/messaging-api/using-quick-reply/) でも、タッチでアクションを登録することができますが、[リッチメニュー切替アクション](https://developers.line.biz/ja/reference/messaging-api/#richmenu-switch-action) を利用できるのは、リッチメニューオブジェクトのみです。
https://developers.line.biz/ja/reference/messaging-api/#action-objects
