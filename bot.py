import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
# from aiogram.filters import 

TOKEN = ""

bot = Bot("")
dp = Dispatcher()

START_MESSAGE = """
Привет! Этот бот позволяет публиковать книги на локальный веб-сервер. Для того, чтобы использовать бота, отправьте ему документ в формате .epub или .pdf.
Бот сам перевесит документ в html и опубликует его на локальном веб-сервере на адресе http://localhost:8000.
"""

async def main():
    await dp.start_polling(bot)


@dp.message(F.text == "/start")
async def hello(message: Message):
    await message.answer(f"привет, {message.from_user.full_name}!")

@dp.message(F.document)
async def document(message: Message):
    try:
        await bot.download(file=message.document.file_id, destination=f"books/{message.document.file_name}")
        await message.answer(f"ваш файл {message.document.file_name} скачен ")
    except:
        await message.answer("не удалось скачать файл т.к его размер превышает 20 мб")

if __name__ == '__main__':
    asyncio.run(main())
