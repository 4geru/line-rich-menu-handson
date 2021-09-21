package main

import (
	"log"

	"github.com/line/line-bot-sdk-go/v7/linebot"
)

// rich_menu_object でリッチメニューの構成を指定する
// リッチメニューオブジェクト: https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object
func createRichMenu(bot *linebot.Client, richMenu linebot.RichMenu) string {
	res, err := bot.CreateRichMenu(richMenu).Do()
	if err != nil {
		log.Fatal(err)
	}
	return res.RichMenuID
}

// リッチメニューに画像をアップロードして添付する
func setRichMenuImage(bot *linebot.Client, richMenuId string, filePath string) {
	if _, err := bot.UploadRichMenuImage(richMenuId, filePath).Do(); err != nil {
		log.Fatal(err)
	}
}

// デフォルトのリッチメニューを設定する
func setDefaultRichMenu(bot *linebot.Client, richMenuId string) {
	if _, err := bot.SetDefaultRichMenu(richMenuId).Do(); err != nil {
		log.Fatal(err)
	}
}

// リッチメニューの alias の登録
func setRichMenuAlias(bot *linebot.Client, richMenuId string, richMenuAliasID string) {
	if _, err := bot.CreateRichMenuAlias(richMenuAliasID, richMenuId).Do(); err != nil {
		log.Fatal(err)
	}
}

func reset(bot *linebot.Client) {
	res, err := bot.GetRichMenuList().Do()
	if err != nil {
		log.Fatal(err)
	}
	for _, richmenu := range res {
		bot.DeleteRichMenu(richmenu.RichMenuID)
	}

	aliasRes, aliasErr := bot.GetRichMenuAliasList().Do()
	if aliasErr != nil {
		log.Fatal(aliasErr)
	}
	for _, alias := range aliasRes {
		if _, err = bot.DeleteRichMenuAlias(alias.RichMenuAliasID).Do(); err != nil {
			log.Fatal(err)
		}
	}
}

func main() {
	bot, err := linebot.New(
		"LINE_CHANNEL_SECRET",   // 上書きする
		"CHANNEL_CHANNEL_TOKEN", // 上書きする
	)
	if err != nil {
		log.Fatal(err)
	}
	reset(bot)

	// 2. リッチメニューA（richmenu-a）を作成する
	richMenuAId := createRichMenu(bot, richMenuObjectA())
	// log.Print(richMenuAId)
	// 3. リッチメニューAに画像をアップロードする
	setRichMenuImage(bot, richMenuAId, "../public/richmenu-a.png")
	// 4. リッチメニューB（richmenu-b）を作成する
	richMenuBId := createRichMenu(bot, richMenuObjectB())
	// log.Print(richMenuBId)
	// 5. リッチメニューBに画像をアップロードする
	setRichMenuImage(bot, richMenuBId, "../public/richmenu-b.png")
	// 6. リッチメニューAをデフォルトのリッチメニューにする
	setDefaultRichMenu(bot, richMenuAId)
	// 7. リッチメニューエイリアスAを作成する
	setRichMenuAlias(bot, richMenuAId, "richmenu-alias-a")
	// 8. リッチメニューエイリアスBを作成する
	setRichMenuAlias(bot, richMenuBId, "richmenu-alias-b")
	log.Printf("success")
}
