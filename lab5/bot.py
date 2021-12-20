import telebot
import cfg
from telebot import types

client = telebot.TeleBot(cfg.config['token'])


@client.message_handler(commands = ['info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data = 'no')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Показать информацию у вас?', 
        reply_markup = markup_inline
    )
        
@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Моё имя')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Выберите, что вам нужно',
            reply_markup = markup_reply
        )
    elif call.data == 'no':
        client.send_message(call.message.chat.id, 'На нет и суда нет😥')
        pass


@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == '/start':    
        client.send_message(message.chat.id, 'Тебя приветсвует бот junglebot4\n Тебе доступна команда /info')

    if message.text.lower() == 'привет':
        client.send_message(message.chat.id, 'Bup, pip')

    if message.text == 'Мой ID':
        client.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}')
    elif message.text == 'Моё имя':
        client.send_message(message.chat.id, f'Ваше Имя: {message.from_user.first_name} {message.from_user.last_name}')

      
client.polling(non_stop = True, interval = 0)

