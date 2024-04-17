import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from APOD import get_APOD
import os

down_dir = "./down_dir"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN.get_secret_value())
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Это NASA бот, пока что он может выводить фото дня от NASA, попробуй! Пиши /APOD")

@dp.message(Command("APOD"))
async def send_APOD(message: types.Message):
    title, explanation, hdurl, copyright, filename = get_APOD()
    photo = types.FSInputFile(down_dir + "/" + filename)
    await bot.send_photo(message.chat.id, photo=photo, caption=f'Название: {title}')
    await message.answer(f"Объяснение: {explanation}\nЕсли хотите скачать фото в лучшем качестве, переходите по ссылке: {hdurl}\nАвторские права: {copyright}")
    os.remove(down_dir + "/" + filename)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

""" title, explanation, hdurl, copyright, filename = get_APOD()
filepath = down_dir + "/" + filename
print(filepath) """