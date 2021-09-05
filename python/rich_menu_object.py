def rich_menu_object_a():
  return {
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": False,
    "name": "richmenu-a",
    "chatBarText": "Tap to open",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 1250,
          "height": 1686
        },
        "action": {
          "type": "uri",
          "uri": "https://developers.line.biz/"
        }
      },
      {
        "bounds": {
          "x": 1251,
          "y": 0,
          "width": 1250,
          "height": 1686
        },
        "action": {
          "type": "richmenuswitch",
          "richMenuAliasId": "richmenu-alias-b",
          "data": "richmenu-changed-to-b"
        }
      }
    ]
  }

def rich_menu_object_b():
  return {
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": False,
    "name": "richmenu-a",
    "chatBarText": "Tap to open",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 1250,
          "height": 1686
        },
        "action": {
          "type": "richmenuswitch",
          "richMenuAliasId": "richmenu-alias-a",
          "data": "richmenu-changed-to-a"
        }
      },
      {
        "bounds": {
          "x": 1251,
          "y": 0,
          "width": 1250,
          "height": 1686
        },
        "action": {
          "type": "uri",
          "uri": "https://developers.line.biz/"
        }
      }
    ]
  }
