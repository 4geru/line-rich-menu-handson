from linebot import (
    LineBotApi,
)

from linebot.models import (
    RichMenu,
    RichMenuArea,
    RichMenuSize,
    RichMenuBounds,
    URIAction
)
from linebot.models.actions import RichMenuSwitchAction
from linebot.models.rich_menu import RichMenuAlias

import rich_menu_object

line_bot_api = LineBotApi('LINE_CHANNEL_TOKEN')

# === 1. 登録されているリッチメニューを確認する ===
def fetch_rich_menus():
    return line_bot_api.get_rich_menu_list()

# 全ての rich menu を確認する
rich_menu_list = fetch_rich_menus()
for rich_menu in rich_menu_list:
    # rich_menu_id を確認する
    # TODO: rich_menu の要素を確認してみましょう！
    print(rich_menu.rich_menu_id)

# === 2. リッチメニューの作成
def create_action(action):
    if action['type'] == 'uri':
        return URIAction(type=action['type'], uri=action.get('uri'))
    else:
        return RichMenuSwitchAction(type=action['type'], rich_menu_alias_id=action.get('richMenuAliasId'), data=action.get('data'))

def create_rich_menus(rich_menu_object):
    areas = [
        RichMenuArea(
            bounds=RichMenuBounds(x=info['bounds']['x'], y=info['bounds']['y'], width=info['bounds']['width'], height=info['bounds']['height']),
            action=create_action(info['action'])
        ) for info in rich_menu_object['areas']
    ]

    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=rich_menu_object['size']['width'], height=rich_menu_object['size']['height']),
        selected=rich_menu_object['selected'],
        name=rich_menu_object['name'],
        chat_bar_text=rich_menu_object['name'],
        areas=areas
    )
    return line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

def set_rich_menu_image(rich_menu_id, rich_menu_image_path):
    with open(rich_menu_image_path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

# object a の作成
rich_menu_a_id = create_rich_menus(rich_menu_object.rich_menu_object_a())
set_rich_menu_image(rich_menu_a_id, '../public/richmenu-a.png')
# object b の作成
rich_menu_b_id = create_rich_menus(rich_menu_object.rich_menu_object_b())
set_rich_menu_image(rich_menu_b_id, '../public/richmenu-b.png')

# === 3. リッチメニューの確認 ===
def get_rich_menu(rich_menu_id):
    return line_bot_api.get_rich_menu(rich_menu_id)

print(get_rich_menu(rich_menu_a_id))

# === 4. リッチメニューの削除 ===
def delete_rich_menu(rich_menu_id):
    return line_bot_api.delete_rich_menu(rich_menu_id)

# print(delete_rich_menu(rich_menu_a_id))
# print(delete_rich_menu(rich_menu_b_id))

# === 5. リッチメニューの alias 登録/削除 ===
def set_rich_menus_alias(rich_menu_id, rich_menus_alias_id):
    alias = RichMenuAlias(
        rich_menu_alias_id=rich_menus_alias_id,
        rich_menu_id=rich_menu_id
    )
    line_bot_api.create_rich_menu_alias(alias)

def unset_rich_menus_alias(rich_menus_alias_id):
    return line_bot_api.delete_rich_menu_alias(rich_menus_alias_id)

set_rich_menus_alias(rich_menu_a_id, 'richmenu-alias-a')
set_rich_menus_alias(rich_menu_b_id, 'richmenu-alias-b')

# === 全てのリッチメニューの削除 ===
rich_menu_list = fetch_rich_menus()
for rich_menu in rich_menu_list:
    delete_rich_menu(rich_menu.rich_menu_id)
