require 'line/bot'
require './rich_menu_object'

def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # 上書きする
      config.channel_token = "LINE_CHANNEL_TOKEN"   # 上書きする
    }
end

# 全てのリッチメニューを取得する
def fetch_rich_menus
  rich_menu_response = client.get_rich_menus
  rich_menus = JSON.parse(rich_menu_response.response.body)["richmenus"]
end

# rich_menu_object でリッチメニューの構成を指定する
# リッチメニューオブジェクト: https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object
def create_rich_menu(rich_menu_object)
  client.create_rich_menu(rich_menu_object)
end

# リッチメニューの画像登録
def set_rich_menu_image(rich_menu_id, rich_menu_image_path)
  client.create_rich_menu_image(rich_menu_id, File.open(rich_menu_image_path))
end

def create_rich_menu_alias(rich_menu_id, rich_menu_alias_id)
  client.set_rich_menus_alias(rich_menu_id, rich_menu_alias_id)
end

# 個別のリッチメニューを取得する
def fetch_rich_menu(rich_menu_id)
  rich_menu_response = client.get_rich_menu(rich_menu_id)
  rich_menus = JSON.parse(rich_menu_response.response.body)
end

# 個別のリッチメニューを削除する
def delete_rich_menu(rich_menu_id)
  client.delete_rich_menu(rich_menu_id)
end

# デフォルトのリッチメニューを作成する
def set_default_rich_menu(rich_menu_id)
  client.set_default_rich_menu(rich_menu_id)
end

def main
  # 2. リッチメニューA（richmenu-a）を作成する
  create_rich_menu_response = create_rich_menu(rich_menu_object_a)
  rich_a_menu = JSON.parse(create_rich_menu_response.body)
  puts "created: #{rich_a_menu}"
  # =>{"richMenuId"=>"richmenu-xxx"}
  # 3. リッチメニューAに画像をアップロードする
  set_rich_menu_image(rich_a_menu['richMenuId'], '../public/richmenu-a.png')
  # 4. リッチメニューB（richmenu-b）を作成する
  create_rich_menu_response = create_rich_menu(rich_menu_object_b)
  rich_b_menu = JSON.parse(create_rich_menu_response.body)
  set_rich_menu_image(rich_b_menu['richMenuId'], '../public/richmenu-b.png')
  puts "created: #{rich_a_menu}"
  # => {"richMenuId"=>"richmenu-xxx"}
  # 5. リッチメニューBに画像をアップロードする
  rich_b_menu = JSON.parse(create_rich_menu_response.body)
  # 6. リッチメニューAをデフォルトのリッチメニューにする
  set_default_rich_menu(rich_a_menu['richMenuId'])
  # 7. リッチメニューエイリアスAを作成する
  create_rich_menu_alias(rich_a_menu['richMenuId'], 'richmenu-alias-a')
  # 8. リッチメニューエイリアスBを作成する
  create_rich_menu_alias(rich_b_menu['richMenuId'], 'richmenu-alias-b')
  puts 'success'
end

main
