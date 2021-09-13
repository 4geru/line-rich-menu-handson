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

// === 1. 登録されているリッチメニューを確認する ===
// 全ての rich menu を確認する
const fetchRichMenu = async () => {
  return await client.getRichMenuList()
}

// === 2. リッチメニューの作成 ===
const createRichMenu = async (richMenuObject) => {
  return await client.createRichMenu(
    richMenuObject
  )
}

const setRichMenuImage = async (richMenuId, path) => {
  const filepath = join(__dirname, path);
  const buffer = readFileSync(filepath);

  const res = await client.setRichMenuImage(richMenuId, buffer);
}

// === 3. リッチメニューの確認 ===
const getRichMenu = async (richMenuId) => {
  return await client.getRichMenu(richMenuId)
}

// === 4. リッチメニューの削除 ===
const deleteRichMenu = async (richMenuId) => {
  return await client.deleteRichMenu(richMenuId)
}

// === 5. リッチメニューの alias 登録/削除 ===
const setRichMenuAlias = async (richMenuId, richMenuAliasId) => {
  return await client.createRichMenuAlias(richMenuId, richMenuAliasId)
}

const unRichMenuAlias = async (richMenuAliasId) => {
  return await client.deleteRichMenuAlias(richMenuAliasId)
}

const setDefaultRichMenu = async (richMenuId) => {
  return await client.setDefaultRichMenu(richMenuId)
}

const main = async () => {
  // === 1. 登録されているリッチメニューを確認する ===
  const response = await fetchRichMenu()
  // === 2. リッチメニューの作成 ===
  const richMenuAId = await createRichMenu(richMenuObjectA())
  const richMenuBId = await createRichMenu(richMenuObjectB())
  console.log({richMenuAId, richMenuBId})
  await setRichMenuImage(richMenuAId, '../public/richmenu-a.png')
  await setRichMenuImage(richMenuBId, '../public/richmenu-b.png')
  // === 3. リッチメニューの確認 ===
  // console.log(await getRichMenu(richMenuAId))
  // console.log(await getRichMenu(richMenuBId))
  // === 4. リッチメニューの削除 ===
  // await deleteRichMenu(richMenuAId)
  // === 5. リッチメニューの alias 登録/削除 ===
  try {
    await setRichMenuAlias(richMenuAId, 'richmenu-alias-a')
  } catch(e) {
    console.log(e)
    console.log('error richmenu-alias-a')
  };
  try {
    await setRichMenuAlias(richMenuBId, 'richmenu-alias-b')
  } catch {
    console.log('error richmenu-alias-b')
  };
  // === 6. リッチメニューのデフォルトの設定 ===
  await setDefaultRichMenu(richMenuBId)
}

const deleteAll = async () => {
  unRichMenuAlias('richmenu-alias-a')
  unRichMenuAlias('richmenu-alias-b')
  const response = await fetchRichMenu()
  for(var res of response) {
    deleteRichMenu(res.richMenuId)
  }
}
deleteAll()
main()
