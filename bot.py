import requests
import json
import os

telegram_api = 'https://api.telegram.org'
telegram_channel = os.environ['CHANNEL_NAME']
telegram_chat_id = os.environ['BOT_CHAT_ID']
telegram_token = os.environ['BOT_TOKEN']
telegram_bot = f'bot{telegram_chat_id}:{telegram_token}'


def send_message(text=''):
    try:
        response = requests.get('%s/%s/%s' % (telegram_api, telegram_bot, 'sendMessage'),
                                params={'chat_id': telegram_channel, 'text': text})
        return json.loads(response.content)
    except Exception as e:
        print(e)
