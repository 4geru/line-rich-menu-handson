// CommonJS
const line = require('@line/bot-sdk');
const { join } = require("path");
const { readFileSync } = require("fs");
const {richMenuObjectA, richMenuObjectB} = require('./rich_menu_object.js');

const config = {
  channelAccessToken: 'LINE_CHANNEL_TOKEN',
  channelSecret: 'LINE_CHANNEL_SECRET'
};

client = new line.Client(config);

const reset = async() => {
  // 全 alias を選択する
  client.getRichMenuAliasList().then((res) => {
    for(var richMenu of res.aliases) {
      // alias を削除する
      client.deleteRichMenuAlias(richMenu.richMenuAliasId)
    }
  })

  // 全リッチメニューを選択する
  client.getRichMenuList().then((res) => {
    for(var richMenu of res) {
      // リッチメニューを削除する
      client.deleteRichMenu(richMenu.richMenuId)
    }
  })
}

// リッチメニューを作成する
const createRichMenu = async (richMenuObject) => {
  return await client.createRichMenu(
    richMenuObject
  )
}

// リッチメニューに画像をアップロードして添付する
const setRichMenuImage = async (richMenuId, path) => {
  const filepath = join(__dirname, path);
  const buffer = readFileSync(filepath);

  const res = await client.setRichMenuImage(richMenuId, buffer);
}

// デフォルトのリッチメニューを設定する
const setRichMenuAlias = async (richMenuId, richMenuAliasId) => {
  return await client.createRichMenuAlias(richMenuId, richMenuAliasId)
}

// デフォルトのリッチメニューを設定する
const setDefaultRichMenu = async (richMenuId) => {
  return await client.setDefaultRichMenu(richMenuId)
}

const main = async () => {
  // 2. リッチメニューA（richmenu-a）を作成する
  const richMenuAId = await createRichMenu(richMenuObjectA())
  // 3. リッチメニューAに画像をアップロードする
  await setRichMenuImage(richMenuAId, '../public/richmenu-a.png')
  // 4. リッチメニューB（richmenu-b）を作成する
  const richMenuBId = await createRichMenu(richMenuObjectB())
  // 5. リッチメニューBに画像をアップロードする
  await setRichMenuImage(richMenuBId, '../public/richmenu-b.png')
  // 6. リッチメニューAをデフォルトのリッチメニューにする
  await setDefaultRichMenu(richMenuBId)
  // 7. リッチメニューエイリアスAを作成する
  await setRichMenuAlias(richMenuAId, 'richmenu-alias-a')
  // 8. リッチメニューエイリアスBを作成する
  await setRichMenuAlias(richMenuBId, 'richmenu-alias-b')
  console.log('success')
}

reset()
main()
