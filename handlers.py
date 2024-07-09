from datetime import datetime

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import sheet, bot, url, image
from keyboard import get_main_keyboard
from payment import get_payment_url

router = Router()


# Обработка команды /start
@router.message(CommandStart())
async def command_start_handler(message: Message):
    # Отправляем приветственное сообщение и отображаем клавиатуру
    await message.reply(text="Здравствуйте! Выберите одну из кнопок", reply_markup=get_main_keyboard())


# Обработка коллбэков (нажатий на кнопки)
@router.callback_query()
async def callback_query(query: CallbackQuery):
    # Обработка нажатия на кнопку 1
    if query.data == "get_address":
        await bot.send_message(query.from_user.id, f"Ленина, 1:\n{url}")
    # Обработка нажатия на кнопку 2
    elif query.data == "pay":
        amount = 2
        description = "Оплата 2 руб"
        payment_url, label = get_payment_url(amount, description)
        await bot.send_message(query.from_user.id, f"Ссылка на оплату 2 руб:\n{payment_url}")
    # Обработка нажатия на кнопку 3
    elif query.data == "get_image":
        await bot.send_photo(query.from_user.id, image, caption="Картинка")
    # Обработка нажатия на кнопку 4
    elif query.data == "get_a2":
        cell_value = sheet.acell('A2').value
        await bot.send_message(query.from_user.id, f"Значение ячейки А2: {cell_value}")


# Обработка текстовых сообщений
@router.message()
async def message_handler(message: Message):
    try:
        # Проверка корректности даты
        date_format = "%d.%m.%y"
        datetime.strptime(message.text, date_format)

        # Добавление даты в следующий пустой ряд столбца B
        next_row = len(sheet.col_values(2)) + 1
        sheet.update_cell(next_row, 2, message.text)

        # Отправка пользователю сообщения о верной дате
        await bot.send_message(message.chat.id, "Дата верна")
    except ValueError:
        # Отправка пользователю сообщения о неверной дате
        await bot.send_message(message.chat.id, "Дата неверна")
