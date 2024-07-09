from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard():
    # Создание экземпляра InlineKeyboardBuilder для создания инлайн-клавиатуры
    builder = InlineKeyboardBuilder()
    # Добавление кнопки 1 - "Ленина 1"
    builder.button(text="Ленина 1", callback_data="get_address")
    # Добавление кнопки 2 - "Оплата 2 руб"
    builder.button(text="Оплата 2 руб", callback_data="pay")
    # Добавление кнопки 3 - "Картинка"
    builder.button(text="Картинка", callback_data="get_image")
    # Добавление кнопки 4 - "Значение А2"
    builder.button(text="Значение А2", callback_data="get_a2")

    # Установка количества кнопок в строке (здесь по одной кнопке на строку)
    builder.adjust(1)

    # Возвращаем готовую инлайн-клавиатуру
    return builder.as_markup()

