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
    await message.answer(f"Document received: {message.document.file_id} file_name {message.document.file_name}")
    await bot.download(file=message.document.file_id, destination=f"books/{message.document.file_name}")


if __name__ == '__main__':
    asyncio.run(main())
