---
title: "node.js"
---

## コードの実行

```shell
npm install
```

## 拡張1. 全てのデータを削除する

:::details 答え
```javascript:index.js
const deleteAll = async () => {
  unRichMenuAlias('richmenu-alias-a')
  unRichMenuAlias('richmenu-alias-b')
  const response = await fetchRichMenu()
  for(var res of response) {
    deleteRichMenu(res.richMenuId)
  }
}
```
:::