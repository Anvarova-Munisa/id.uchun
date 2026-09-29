from aiogram import Router, types, F

router = Router()


@router.message(F.voice)
async def voice(message: types.Message):
    await message.answer(message.voice.file_id)