import telebot
from telebot import types

# Жаңы токениңиз
TOKEN = '8929956516:AAGUYLoszpYIUCBePNC0cqfMhMH1xkkcbnc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🔥 Каналга өтүү", url="https://t.me/telegram")
    btn2 = types.InlineKeyboardButton("❤️ Лайк", callback_data="like")
    markup.add(btn1)
    markup.add(btn2)
    
    bot.send_message(
        message.chat.id, 
        "👋 **Салам! Бот ийгиликтүү иштеп баштады!**\n\nКаналыңызга чыгара турган текстти жөнөтүңүз, мен ага баскычтарды кошуп берем.", 
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🔥 Подписаться", url="https://t.me/telegram")
    markup.add(btn1)
    
    bot.send_message(
        message.chat.id, 
        f"✨ **Сиздин постуңуз:**\n\n{message.text}", 
        reply_markup=markup
    )

if __name__ == "__main__":
    bot.infinity_polling()
