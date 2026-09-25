from aiogram.types import CopyTextButton, WebAppInfo, SwitchInlineQueryChosenChat
from aiogram.utils.keyboard import InlineKeyboardBuilder

def tugma():
    b = InlineKeyboardBuilder()
    b.button(text="oddiy",callback_data="oddiy")
    b.button(text="mashinalar",callback_data="car")
    # b.button(text="you tube",url="")
    # b.button(text="card",copy_text=CopyTextButton(text=""))
    # b.button(text="",web_app=WebAppInfo(url=""))
    b.button(text="ulashish",switch_inline_query="mashinalar")
    b.button(text="kanalga ulashish",switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
        query="new car",
        allow_user_chats=True,

    ))

    b.button(text="gurpaga ulashish", switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
        query="new group",
        allow_group_chats=True,

    ))

    b.button(text="kanalga ulashish", switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
        query="new channel",
        allow_channel_chats=True,

    ))
    b.button(text="botga ulashish", switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
        query="new bot",
        allow_bot_chats=True,

    ))

    b.adjust(3)
    return b.as_markup(resize_keyboard=True)
cars = ["cobalt","lasetti","BMW","tiko","damas","nexia"]
def car():
    b = InlineKeyboardBuilder()
    for car in cars:
        b.button(text=car.capitalize(),callback_data=f"tanlandi_{car}")
        b.adjust(3)
    return b.as_markup()