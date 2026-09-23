from datetime import datetime, timedelta
from aiogram import Router, types

router = Router()


# @router.message()
# async def button(msg: types.Message):
#     vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     if msg.users_shared:
#         users = msg.users_shared.users
#         ismlar, familyalar, usernamelar, idlar = [], [], [], []
#         son = 0
#         for user in users:
#             ismlar.append(user.first_name)
#             familyalar.append(user.last_name)
#             usernamelar.append(user.username)
#             idlar.append(user.user_id)
#             son += 1
#         for i in range(son):
#              n = f"#user\n"
#              n += f"user: {ismlar[i]} {familyalar[i]}\n"
#              n += f"Username: @{usernamelar[i]}\n"
#              n +=f"ID: {idlar[i]}\n\n"
#              n += f"sana va vaqt: {vaqt}"
#              await msg.answer(n)


@router.message()
async def button(msg: types.Message):
    vaqt = (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")
    if msg.users_shared:
        users = msg.users_shared.users
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for user in users:
            ismlar.append("Foydalanuvchi")
            familyalar.append("")
            usernamalar.append("yo'q")
            idlar.append(user.user_id)
            son += 1

        for i in range(son):
            n = f"#user\n"
            n += f"user: {ismlar[i]} {familyalar[i]}\n"
            n += f"Username: @{usernamalar[i]}\n"
            n += f"ID: {idlar[i]}\n\n"
            n += f"sana va vaqt: {vaqt}"
            await msg.answer(n)

    elif msg.chat_shared and msg.chat_shared.request_id == 3:
        groups = [msg.chat_shared]
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for group in groups:
            ismlar.append("Guruh")
            familyalar.append("")
            usernamalar.append("yo'q")
            idlar.append(group.chat_id)
            son += 1

        for i in range(son):
            n = f"#group\n"
            n += f"group: {ismlar[i]} {familyalar[i]}\n"
            n += f"Username: @{usernamalar[i]}\n"
            n += f"ID: {idlar[i]}\n\n"
            n += f"sana va vaqt: {vaqt}"
            await msg.answer(n)

    elif msg.chat_shared and msg.chat_shared.request_id == 4:
        chanels = [msg.chat_shared]
        ismlar, familyalar, usernamalar, idlar = [], [], [], []
        son = 0
        for chanel in chanels:
            ismlar.append("Kanal")
            familyalar.append("")
            usernamalar.append("yo'q")
            idlar.append(chanel.chat_id)
            son += 1

        for i in range(son):
            n = f"#chanel\n"
            n += f"chanel: {ismlar[i]} {familyalar[i]}\n"
            n += f"Username: @{usernamalar[i]}\n"
            n += f"ID: {idlar[i]}\n\n"
            n += f"sana va vaqt: {vaqt}"
            await msg.answer(n)


