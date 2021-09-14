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

def reset():
    # 全 alias を選択する
    rich_menu_list = line_bot_api.get_rich_menu_list()
    for rich_menu in rich_menu_list:
        # alias を削除する
        line_bot_api.delete_rich_menu(rich_menu_id)

    # 全リッチメニューを選択する
    for rich_menu_alias in line_bot_api.get_rich_menu_alias_list().aliases:
        # リッチメニューを削除する
        line_bot_api.delete_rich_menu_alias(rich_menus_alias_id)

# アクションの登録
def create_action(action):
    if action['type'] == 'uri':
        return URIAction(type=action['type'], uri=action.get('uri'))
    else:
        return RichMenuSwitchAction(type=action['type'], rich_menu_alias_id=action.get('richMenuAliasId'), data=action.get('data'))

# リッチメニューを作成する
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

# リッチメニューに画像をアップロードする
def set_rich_menu_image(rich_menu_id, rich_menu_image_path):
    with open(rich_menu_image_path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

# リッチメニューの alias の登録
def set_rich_menus_alias(rich_menu_id, rich_menus_alias_id):
    alias = RichMenuAlias(
        rich_menu_alias_id=rich_menus_alias_id,
        rich_menu_id=rich_menu_id
    )
    line_bot_api.create_rich_menu_alias(alias)

# デフォルトのリッチメニューを設定する
def set_default_rich_menu(rich_menu_id):
    line_bot_api.set_default_rich_menu(rich_menu_id)

def main():
    # 2. リッチメニューA（richmenu-a）を作成する
    rich_menu_a_id = create_rich_menus(rich_menu_object.rich_menu_object_a())
    # 3. リッチメニューAに画像をアップロードする
    set_rich_menu_image(rich_menu_a_id, '../public/richmenu-a.png')
    # 4. リッチメニューB（richmenu-b）を作成する
    rich_menu_b_id = create_rich_menus(rich_menu_object.rich_menu_object_b())
    # 5. リッチメニューBに画像をアップロードする
    set_rich_menu_image(rich_menu_b_id, '../public/richmenu-b.png')
    # 6. リッチメニューAをデフォルトのリッチメニューにする
    set_default_rich_menu(rich_menu_a_id)
    # 7. リッチメニューエイリアスAを作成する
    set_rich_menus_alias(rich_menu_a_id, 'richmenu-alias-a')
    # 8. リッチメニューエイリアスBを作成する
    set_rich_menus_alias(rich_menu_b_id, 'richmenu-alias-b')
    print('success')

reset()
main()