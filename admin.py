from aiogram import types, Dispatcher
from config import bot, ADMIN

async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.reply("Закрепить сообщение")
        if not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id
                                               )
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name} "
                f"сообщение закреплено {message.from_user.full_name}"
            )
    else:
        await message.answer("Это работает только в группах!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["pin"], commands_prefix="!pin")
