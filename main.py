from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="1882773639:AAEjuA8FqHpMAZGk01yLNaJEbzvQ7JK47Hk")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    # text = "Какой-то текст"
    #
    # send_message = await bot.send_message(chat_id=chat_id, text=text)
    # print(send_message.to_python())
    # sent_message = await bot.send_photo(chat_id=chat_id,photo="https://dj-x.info/uploads/posts/2016-05/1462561296_d09ad0bed182d0b8d0ba-1.jpg")

    sent_message = await bot.set_chat_title(chat_id=chat_id, title="Группа котиков")
    print(sent_message)

    # print(sent_message.photo[-1].file_unique_id)


executor.start_polling(dp)

