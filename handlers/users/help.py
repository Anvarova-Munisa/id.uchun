from aiogram import Router,types
from aiogram.filters import Command
router = Router()

@router.message(Command("help"))
async def help(msg: types.Message):
    n = "kamandalar foydalanish uchun:\n"
    n += "/button\n"
    await msg.reply(n)