from aiogram import Router,types,filters
router = Router()
@router.message()
async def test(msg: types.Message):
   if msg.voice:
       print(msg.voice.file_id)