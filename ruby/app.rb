require 'line/bot'

def client
    @client ||= Line::Bot::Client.new { |config|
      config.channel_secret = "LINE_CHANNEL_SECRET" # need to update
      config.channel_token = "LINE_CHANNEL_TOKEN" # need to update
    }
end

