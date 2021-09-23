require 'line/bot'
require 'json'

def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # 上書きする
      config.channel_token = "LINE_CHANNEL_TOKEN"   # 上書きする
    }
end

# === リッチメニューの情報を見る ===
response = client.get_rich_menus
richmenu_list = JSON.parse(response.body).dig('richmenus')
richmenu_list.each do |richmenu|
  p richmenu['richMenuId'], richmenu
end
user_id = 'Uxxxxxx'
richmenu_id = 'richmenu-xxx'

# # === 個別リッチメニューリンク ===
# client.link_user_rich_menu(user_id, richmenu_id)
# p client.get_user_rich_menu(user_id)
# client.unlink_user_rich_menu(user_id)

# # === 一括リッチメニューリンク ===
# client.bulk_link_rich_menus([user_id], richmenu_id)
# p client.get_user_rich_menu(user_id)
# client.bulk_unlink_rich_menus([user_id])
