from aiogram import Router,types,filters
router = Router()
@router.message(filters.Command("start",prefix="%.+/-="))
async def test(msg: types.Message):
    n = "Xush kelibsiz siz bu bot oraqli , foydalanuvchi nom,guruh va kanal,idsini olaolasz"
    n += " agar  yordam kerak bolsa /help tugmasini bosing"
    await msg.answer(n)
