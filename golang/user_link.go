package main

import (
	"log"

	"github.com/line/line-bot-sdk-go/v7/linebot"
)

func main() {
	bot, err := linebot.New(
		"LINE_CHANNEL_SECRET", // 上書きする
		"LINE_CHANNEL_TOKEN",  // 上書きする
	)
	if err != nil {
		log.Fatal(err)
	}

	// === リッチメニューの情報を見る ===
	if res, _ := bot.GetRichMenuList().Do(); res != nil {
		for _, richmenu := range res {
			log.Printf("%v\n", richmenu)
		}
	}

	// userId := "Uxxxxxx"
	// richmenuId := "richmenu-xxx"

	// // === 個別リッチメニューリンク ===
	// if res, _ := bot.LinkUserRichMenu(userId, richmenuId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }

	// if res, _ := bot.GetUserRichMenu(userId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }

	// if res, _ := bot.UnlinkUserRichMenu(userId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }

	// // === 一括リッチメニューリンク ===
	// if res, _ := bot.BulkLinkRichMenu(richmenuId, userId, userId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }

	// if res, _ := bot.GetUserRichMenu(userId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }

	// if res, _ := bot.BulkUnlinkRichMenu(userId, userId).Do(); res != nil {
	// 	log.Printf("Response %v;", res)
	// }
}
