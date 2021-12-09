from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest


# Your API ID, hash and session string here
api_id = int('')
api_hash = ""
client = TelegramClient('session_name', api_id, api_hash)


client.start()

def test_message():
    try:
        client.send_message('@MIEMConverter_bot', '/start')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '/convert')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '/get_coffee_picture')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '/update_math_skills')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '/get_smart_quote')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '/shakal_picture')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', 'йцукенгшщз')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '1.png')
    except:
        print('error')
    try:
        client.send_message('@MIEMConverter_bot', '❤️')
    except:
        print('error')

if __name__ == "__main__":
    test_message()