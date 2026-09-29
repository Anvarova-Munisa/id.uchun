from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from handlers.users.test import router as test
from handlers.inline.gif import router as gif_router
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.button import router as button_router
from config.settings import BOT_TOKEN
from handlers.users.tugma import router as tugma
from handlers.inline.photo import router as photo
from handlers.inline.audio import router as audio
from handlers.inline.video import router as video
from handlers.inline.voice import router as voice
from handlers.inline.contact import router as contact
from handlers.inline.dakument import router as dakument
from handlers.inline.location import router as location



dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # dp.include_router(test)
    dp.include_router(start_router)
    dp.include_router(help_router)
    # dp.include_router(button_router)
    # dp.include_router(tugma)
    # dp.include_router(photo)
    # dp.include_router(gif_router)
    dp.include_router(dakument)
    dp.include_router(contact)
    dp.include_router(location)
    dp.include_router(audio)
    dp.include_router(video)
    dp.include_router(voice)



    print("Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())