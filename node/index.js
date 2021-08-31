// CommonJS
const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: 'LINE_CHANNEL_TOKEN',
  channelSecret: 'LINE_CHANNEL_SECRET'
};

client = new line.Client(config);

client.getRichMenuList().then((e) => {
  console.log(e)
})
