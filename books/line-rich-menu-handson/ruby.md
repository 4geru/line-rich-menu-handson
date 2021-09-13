---
title: "ruby"
---

## コードの実行

```shell
bundle install
```

```ruby:app.rb
def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # need to update
      config.channel_token = "LINE_CHANNEL_TOKEN" # need to update
    }
end
```

```shell
bundle exec ruby app.rb
```

## 拡張1. 全てのデータを削除する

:::details 答え
```ruby:app.rb
fetch_rich_menus.map do |rich_menu|
  p rich_menu['richMenuId']
  delete_rich_menu(rich_menu['richMenuId'])
end
```
:::