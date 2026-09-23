from datetime import datetime, timedelta
from aiogram import Router, types
router = Router()
@router.message()
async def button(msg: types.Message):
    vaqt = (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")
    if msg.users_shared:
        users = msg.users_shared.users
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for user in users:
            ismlar.append(user.first_name)
            familyalar.append(user.last_name)
            usernamalar.append(user.username)
            idlar.append(user.user_id)
            son += 1

        for i in range(son):
            n = f"#user\n"
            n += f"Nomi: {ismlar[i]} {familyalar[i] or ''}\n"
            n += f"Username: @{usernamalar[i] or 'None'}\n"
            n += f"ID: {idlar[i]}\n"
            n += f"Vaqt: {vaqt}"
            await msg.answer(n)
    elif msg.chat_shared and msg.chat_shared.request_id == 3:
        groups = [msg.chat_shared]
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for group in groups:
            ismlar.append(group.title)
            familyalar.append(None)
            usernamalar.append(group.username)
            idlar.append(group.chat_id)
            son += 1

        for i in range(son):
            n = f"#group\n"
            n += f"Nomi: {ismlar[i]}\n"
            n += f"Username: @{usernamalar[i] or 'None'}\n"
            n += f"ID: {idlar[i]}\n"
            n += f"Vaqt: {vaqt}"
            await msg.answer(n)
    elif msg.chat_shared and msg.chat_shared.request_id == 4:
        channels = [msg.chat_shared]
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for channel in channels:
            ismlar.append(channel.title)
            familyalar.append(None)
            usernamalar.append(channel.username)
            idlar.append(channel.chat_id)
            son += 1
        for i in range(son):
            n = f"#channel\n"
            n += f"Nomi: {ismlar[i]}\n"
            n += f"Username: @{usernamalar[i] or 'None'}\n"
            n += f"ID: {idlar[i]}\n"
            n += f"Vaqt: {vaqt}"
            await msg.answer(n)
