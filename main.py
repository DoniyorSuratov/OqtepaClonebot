import logging
from aiogram import Bot, Dispatcher, executor, types
from bot.dispatcher import dp
from bot.handlers import delivery_handler,start_handler,settings_handler,take_away, menu_handlers




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)