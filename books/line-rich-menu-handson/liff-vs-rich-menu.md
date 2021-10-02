---
title: "LIFFとリッチメニューの違い"
---

## LIFF とは

> LINE Front-end Framework（LIFF）は、LINEが提供するウェブアプリのプラットフォームです。このプラットフォームで動作するウェブアプリを、LIFFアプリと呼びます。

公式：[ドキュメント > LINE Front-end Framework > LINE Front-end Framework](https://developers.line.biz/ja/docs/liff/overview/)

- ブラウザでLINEの機能が使えるフレームワークです。
  - ユーザー情報
  - OS/言語情報 等
  - Botとの友達情報
  - メッセージ送信（LINE内ブラウザのみ）
  - QRスキャン

### LIFFのメリット
- Webのフレームワークを使うことができる
  - 自由度が高い
  - HTMLのフォームが使える
- スマホの外部ブラウザ/PCから利用できる

### リッチメニューのメリット
- 簡単なボタンを表示することができる
  - 誰でも触りやすい
- メッセージを送信したときに、リッチメニューに隠れない
  - LIFFの場合、ブラウザ部分に隠れてしまう
  - 例えば、複数人でゲームアプリを作成した場合に、同期的な処理をすることができる
- botとのメッセージ画面にデフォルトで表示される
  - 興味を引きやすい

## LIFF(LINE Frontend Framework) vs リッチメニュー
LIFFとリッチメニューと自由度- UIとしてどっちがいいんだっけ？みたいな話があると思います。

| | LIFF | リッチメニュー |
| :--- | :--- | :--- |
| メッセージ送信 | ○ | ○ |
| ユーザー情報 | ○ | ○ |
| LINE URLスキーム が使える ※1| ○ | ○ |
| UIの自由度 | ○ | △ |
| LINE のトークが見える | △ | ○ |
| アクションまでの導線 | △ | ○

※1 [LINE URLスキームでLINEの機能を使う](https://developers.line.biz/ja/docs/messaging-api/using-line-url-scheme)
