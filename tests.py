from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time




# Your API ID, hash and session string here
api_id = int('')
api_hash = ""
client = TelegramClient('session_name', api_id, api_hash)


client.start()


class TG_test(unittest.TestCase):
    def testStart(self):
        try:
            client.send_message('@MIEMConverter_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, добро пожаловать в MIEMUniversalBot 🤩 \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/convert - команда для конвертации валюты!\n/get_coffee_picture - команда для получения рандомной картинки кофе!\n/update_math_skills - команда для прокачки большого ума!\n/get_smart_quote - команда для получения пищи для размышлений!\n\/shakal_picture - команда для шакалинга картинки!'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testcofe(self):
        try:
            client.send_message('@MIEMConverter_bot', 'Хочу кофе')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вот ваша фоточка прекрасного напитка'
            self.assertRegex(m, text)
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testum(self):
        try:
            time.sleep(2)
            client.send_message('@MIEMConverter_bot', 'Хочу поумничать перед друзьями')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Как однажды сказал'
            self.assertRegex(m, text)
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testphoto(self):
        try:
            time.sleep(2)
            client.send_message('@MIEMConverter_bot', 'Надо чето с картинкой подшаманить ')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Отправьте картинку, которую надо зашакалить Ꮗ'
            self.assertRegex(m, text)
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testmath(self):
        try:
            time.sleep(2)
            client.send_message('@MIEMConverter_bot', 'Надо к матану готовиться')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вам предлагается решить данный пример для увеличения своей скорости счета, чем быстрее решите, тем лучше!'
            self.assertRegex(m, text)
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)
    def testdollar(self):
        try:
            time.sleep(2)
            client.send_message('@MIEMConverter_bot', 'Мне бы валюту конвертировать 💶')
            time.sleep(2)
            messages = client.get_messages('@MIEMConverter_bot')
            for message in client.get_messages('@MIEMConverter_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'fathutnik, выберите интересующую вас валютную пару для перевода или впишите свою 🤩'
            self.assertRegex(m, text)
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
            client.send_message('@MIEMConverter_bot', 'Хочу в начало')
        except:
            self.assertFalse(True)



















