---
title: "python"
---

## コードの実行

```shell
pipenv install
```

```python:main.py
line_bot_api = LineBotApi('LINE_CHANNEL_TOKEN')
```

```shell
pipenv run python main.py
```

## 拡張1. 全てのデータを削除する

:::details 答え
```python:main.py
rich_menu_list = fetch_rich_menus()
for rich_menu in rich_menu_list:
    delete_rich_menu(rich_menu.rich_menu_id)

print(line_bot_api.get_rich_menu_alias_list().aliases)
for rich_menu_alias in line_bot_api.get_rich_menu_alias_list().aliases:
    print(unset_rich_menus_alias(rich_menu_alias.rich_menu_alias_id))
```
:::