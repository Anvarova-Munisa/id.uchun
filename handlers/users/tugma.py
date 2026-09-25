from aiogram import Router,filters,types,F
from keyboards.inlainKeyboard.tugmaKeyboard import tugma,car
router = Router()

@router.message(filters.Command("tugma"))
async def button(msg:types.Message):
    await msg.answer("tugmalardan birini tanlang",reply_markup=tugma())

@router.callback_query(F.data == "oddiy")
async def oddiy(callback:types.CallbackQuery):
    await callback.answer("mazza qildingizmi",show_alert=True)
    # await callback.message.edit_text("yana tanlashga aqliz yetadimi",reply_markup=tugma())
    # await callback.message.delete()

# @router.callback_query(F.data == "car")
# async def car2(callback:types.CallbackQuery):
#     await callback.answer("mashinalardan birini tanlang",reply_markup=car())
# @router.callback_query(F.data == "tanlandi_")
# async def tanlandi(callback:types.CallbackQuery):
#     car_name = callback.data.replace("tanlandi_","")
#     await callback.answer(" nasib qilsin")


@router.callback_query(F.data == "car")
async def car2(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Mashinalardan birini tanlang", reply_markup=car())
@router.callback_query(F.data.startswith("tanlandi_"))
async def tanlandi1(callback: types.CallbackQuery):
    car_name = callback.data.replace("tanlandi_", "")
    await callback.answer(f"{car_name.capitalize()} nasib qilsin!", show_alert=True)