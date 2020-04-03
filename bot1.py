import telebot
import random

bot = telebot.TeleBot('1129979286:AAErM3Y-o7JLY-jBEaBxXuttTaG79_BHiQA')
f=random.randrange(5,25)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привіт!', 'Поміряти пісюн', 'Знайти щура')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8hF6EkNHYVsfRFto2lycu36MVxCenAAIVAANlpDIU9QmVaqMnu3AYBA', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привіт!':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8gl6Ej_J3duh-ib0_XQkdG8w0ZM8nAAIuAANlpDIUo11rOhNxjqQYBA')
    elif message.text.lower() == 'поміряти пісюн':
        bot.send_message(message.chat.id,  'Твій пісюн '+ str(random.randrange(5,25)) + ' см')
    elif message.text.lower() == 'знайти щура':
        bot.send_sticker(message.chat.id,  'CAACAgIAAxkBAAI8hl6Ek4cH-OPF4h06FnC0_oBlus3WAAIwAANlpDIU2CIRaOdzqOkYBA')
        
        




bot.polling()
