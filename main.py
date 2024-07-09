import asyncio
import logging

from config import dp, bot
from handlers import router


async def main():
    # Настройка логирования для отображения информации в консоли
    logging.basicConfig(level=logging.INFO)

    # Включение маршрутизатора (router) для обработки сообщений и колбэков
    dp.include_router(router)

    # Запуск бота в режиме постоянного опроса новых сообщений
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Запуск основной функции для старта бота
    asyncio.run(main())
