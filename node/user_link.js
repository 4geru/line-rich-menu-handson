// CommonJS
const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: 'LINE_CHANNEL_TOKEN', // 上書きする
  channelSecret: 'LINE_CHANNEL_SECRET'      // 上書きする
};
client = new line.Client(config);

const main = async (client) => {
  // === リッチメニューの情報を見る
  await client.getRichMenuList().then((r) => {
    console.log(r)
  })

  userId = 'Uxxxxxx'
  richmenuId = 'richmenu-xxx'

  // // === 個別リッチメニューリンク ===
  // await client.linkRichMenuToUser(userId, richmenuId).then(() => {}, () => {})
  // await client.getRichMenuIdOfUser(userId).then((r) => {
  //   console.log(r)
  // })
  // await client.unlinkRichMenuFromUser(userId)

  // // === 一括リッチメニューリンク ===
  // await client.linkRichMenuToMultipleUsers(richmenuId, [userId]).then(() => {}, () => {})
  // await client.getRichMenuIdOfUser(userId).then((r) => {
  //   console.log(r)
  // })
  // await client.unlinkRichMenusFromMultipleUsers([userId])
}
main(client)
