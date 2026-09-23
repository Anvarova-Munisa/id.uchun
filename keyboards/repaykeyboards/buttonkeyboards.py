from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
                     KeyboardButtonRequestUsers,
                     KeyboardButtonRequestChat)
def button():
    b = ReplyKeyboardBuilder()
    b.button(text="user",request_users=KeyboardButtonRequestUsers(
        request_id=1,
        user_is_bot=False,
        user_is_premium=False,
        max_quantity=10,
        request_name=True,
        request_username=True,
        request_photo=True,

    ))
    b.button(text="bot", request_users=KeyboardButtonRequestUsers(
        request_id=2,
        user_is_bot=True,
        user_is_pemium=False,
        max_quantity=10,
        request_name=True,
        request_username=True,
        request_photo=False,
    ))
    b.button(text="groups",request_chat=KeyboardButtonRequestChat(
        request_id=3,
        request_title=True,
        request_username = True,
        request_photo = True,


        # chat_is_channel=False,
        # chat_is_forum=False,
        # chat_has_username=False,
        # chat_is_created=False,
        # request_title=True,
        # bot_is_member=True,
        # request_username=True,
        # request_photo=True,

    ))
    b.button(text="channels", request_chat=KeyboardButtonRequestChat(
        request_id=4,
        chat_is_channel=True,
        request_title=True,
        request_username = True,
        request_photo = True,
    ))

    b.adjust(2)
    return b.as_markup(resize_keyboard=True)