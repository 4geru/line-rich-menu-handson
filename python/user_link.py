from linebot import (
    LineBotApi,
)

line_bot_api = LineBotApi('LINE_CHANNEL_TOKEN') # 上書きする

# === リッチメニューの情報を見る ===
for rich_menus in line_bot_api.get_rich_menu_list():
  print(rich_menus.rich_menu_id)

user_id = 'Uxxxxxx'
richmenu_id = 'richmenu-xxx'

# # === 個別リッチメニューリンク ===
# line_bot_api.link_rich_menu_to_user(user_id, richmenu_id)
# print(line_bot_api.get_rich_menu_id_of_user(user_id))
# line_bot_api.unlink_rich_menu_from_user(user_id)

# # === 一括リッチメニューリンク ===
# line_bot_api.link_rich_menu_to_users([user_id], richmenu_id)
# print(line_bot_api.get_rich_menu_id_of_user(user_id))
# line_bot_api.unlink_rich_menu_from_users([user_id])
