package main

import "github.com/line/line-bot-sdk-go/v7/linebot"

func richMenuObjectA() linebot.RichMenu {
	return linebot.RichMenu{
		Size:        linebot.RichMenuSize{Width: 2500, Height: 1686},
		Selected:    false,
		Name:        "richmenu-a",
		ChatBarText: "Tap to open",
		Areas: []linebot.AreaDetail{
			{
				Bounds: linebot.RichMenuBounds{X: 0, Y: 0, Width: 1250, Height: 1686},
				Action: linebot.RichMenuAction{
					Type: linebot.RichMenuActionTypeURI,
					URI:  "https://linedevelopercommunity.connpass.com/event/223972/",
					Text: "click me",
				},
			},
			{
				Bounds: linebot.RichMenuBounds{X: 1251, Y: 0, Width: 1250, Height: 1686},
				Action: linebot.RichMenuAction{
					Type:            linebot.RichMenuActionTypeRichMenuSwitch,
					RichMenuAliasID: "richmenu-alias-b",
					Data:            "action=richmenu-changed-to-b",
				},
			},
		},
	}
}

func richMenuObjectB() linebot.RichMenu {
	return linebot.RichMenu{
		Size:        linebot.RichMenuSize{Width: 2500, Height: 1686},
		Selected:    false,
		Name:        "richmenu-a",
		ChatBarText: "Tap to open",
		Areas: []linebot.AreaDetail{
			{
				Bounds: linebot.RichMenuBounds{X: 0, Y: 0, Width: 1250, Height: 1686},
				Action: linebot.RichMenuAction{
					Type:            linebot.RichMenuActionTypeRichMenuSwitch,
					RichMenuAliasID: "richmenu-alias-a",
					Data:            "action=richmenu-changed-to-a",
				},
			},
			{
				Bounds: linebot.RichMenuBounds{X: 1251, Y: 0, Width: 1250, Height: 1686},
				Action: linebot.RichMenuAction{
					Type: linebot.RichMenuActionTypeURI,
					URI:  "https://linedevelopercommunity.connpass.com/event/223972/",
					Text: "click me",
				},
			},
		},
	}
}
