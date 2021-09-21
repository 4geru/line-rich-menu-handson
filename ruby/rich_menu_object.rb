def rich_menu_object_a
  {
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
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
          "uri": "https://linedevelopercommunity.connpass.com/event/223972/"
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
end

def rich_menu_object_b
  {
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
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
          "uri": "https://linedevelopercommunity.connpass.com/event/223972/"
        }
      }
    ]
  }
end
