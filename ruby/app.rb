require 'line/bot'

def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # 上書きする
      config.channel_token = "LINE_CHANNEL_TOKEN"   # 上書きする
    }
end

# === 1. 登録されているリッチメニューを確認する ===
# 全てのリッチメニューを取得する
def fetch_rich_menus
  rich_menu_response = client.get_rich_menus
  rich_menus = JSON.parse(rich_menu_response.response.body)["richmenus"]
end

# p fetch_rich_menus
# => []

# === 2. リッチメニューの作成 ===
# rich_menu_object でリッチメニューの構成を指定する
# リッチメニューオブジェクト: https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object
def create_rich_menu(rich_menu_object)
  client.create_rich_menu(rich_menu_object)
end

# リッチメニューの画像登録
def set_rich_menu_image(rich_menu_id, rich_menu_image_path)
  client.create_rich_menu_image(rich_menu_id, File.open(rich_menu_image_path))
end

require './rich_menu_object'
# # rich menu a を作る
create_rich_menu_response = create_rich_menu(rich_menu_object_a)
rich_a_menu = JSON.parse(create_rich_menu_response.body)
p rich_a_menu
# # => => {"richMenuId"=>"richmenu-xxx"}
set_rich_menu_image(rich_a_menu['richMenuId'], '../public/richmenu-a.png')
# # rich menu b を作る
create_rich_menu_response = create_rich_menu(rich_menu_object_b)
rich_b_menu = JSON.parse(create_rich_menu_response.body)
set_rich_menu_image(rich_b_menu['richMenuId'], '../public/richmenu-b.png')
# p rich_menu
# # => => {"richMenuId"=>"richmenu-xxx"}

# === 3. リッチメニューの確認 ===
# 個別のリッチメニューを取得する
def fetch_rich_menu(rich_menu_id)
  rich_menu_response = client.get_rich_menu(rich_menu_id)
  rich_menus = JSON.parse(rich_menu_response.response.body)
end

# response = fetch_rich_menu(rich_menu['richMenuId'])
# p response

# === 4. リッチメニューの削除 ===
# 個別のリッチメニューを削除する
def delete_rich_menu(rich_menu_id)
  client.delete_rich_menu(rich_menu_id)
end

# === 6. リッチメニューのデフォルトの設定 ===
# p delete_rich_menu(response['richMenuId'])
def set_default_rich_menu(rich_menu_id)
  client.set_default_rich_menu(rich_menu_id)
end

set_default_rich_menu(rich_a_menu['richMenuId'])
