import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Жаңы Telegram API Токениңиз
API_TOKEN = '8929956516:AAGUYLoszpYIUCBePNC0cqfMhMH1xkkcbnc'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start командасы
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 **Каналды кооздоочу ботко кош келиңиз!**\n\n"
        "Мага каналыңызга чыгара турган **текстти, сүрөттү же видеону** жөнөтүңүз, мен ага атайын астынкы баскычтарды (кнопкаларды) кошуп берем."
    )

# Колдонуучу билдирүү же медиа жөнөткөндө баскычтарды кошуу
@dp.message()
async def prepare_post(message: types.Message):
    builder = InlineKeyboardBuilder()
    
    # Инлайн баскычтар (Каналга шилтеме жана реакция)
    builder.button(text="🔥 Каналга жазылуу", url="https://t.me/telegram")
    builder.button(text="❤️ Лайк (100)", callback_data="like_pressed")
    builder.adjust(1)  # Баскычтарды астын-үстүн жайгаштыруу

    post_text = message.text or message.caption or ""
    
    await message.answer(
        "✨ **Сиздин постуңуздун даяр көрүнүшү:**\n\n" + post_text,
        reply_markup=builder.as_markup()
    )
    await message.answer("💡 *Ушул постту өз каналыңызга репост кылып жөнөтсөңүз болот!*")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
