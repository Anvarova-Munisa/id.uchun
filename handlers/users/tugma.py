from aiogram import Router,filters,types,F
from keyboards.inlainKeyboard.tugmaKeyboard import tugma,car,rang,tasdiqlash

router = Router()

@router.message(filters.Command("tugma"))
async def button(msg:types.Message):
    await msg.answer("tugmalardan birini tanlang",reply_markup=tugma())

@router.callback_query(F.data == "oddiy")
async def oddiy(callback:types.CallbackQuery):
    await callback.answer("mazza qildingizmi")
    # await callback.message.edit_text("yana tanlashga aqliz yetadimi",reply_markup=tugma())
    # await callback.message.delete()

@router.callback_query(F.data == "car")
async def car2(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Mashinalardan birini tanlang", reply_markup=car())
@router.callback_query(F.data.startswith("tanlandi_"))
async def tanlandi1(callback: types.CallbackQuery):
    car_name = callback.data.replace("tanlandi_", "")
    await callback.answer(f"{car_name.capitalize()} nasib qilsin!")
    await callback.message.edit_text("Rangni tanlang", reply_markup=rang())

@router.callback_query(F.data.startswith("tanlandi_"))
async def tanlandi1(callback: types.CallbackQuery):
    car_name = callback.data.replace("tanlandi_", "")
    await callback.answer(f"{car_name.capitalize()} nasib qilsin!")
    await callback.message.edit_text("Rangni tanlang", reply_markup=rang())


@router.callback_query(F.data.startswith("rang"))
async def rang_tanlandi(callback: types.CallbackQuery):
    color = callback.data.replace("rang", "")
    await callback.answer(f"Rang: {color.capitalize()} tanlandi")
    await callback.message.edit_text("Buyurtma berasizmi?", reply_markup=tasdiqlash())

@router.callback_query(F.data == "ha")
async def ha_tanlandi(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Tanlovingiz uchun rahmat! Sizga tez orada aloqaga chiqamiz.")


@router.callback_query(F.data == "yoq")
async def yoq_tanlandi(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Xo'p")


@router.callback_query(F.data == "senga nma")
async def qiziqib_kirgan(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Ok")

