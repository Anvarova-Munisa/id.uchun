from aiogram import Router, types, F

router = Router()
audiolar = [
    "CQACAgQAAxkBAAPAaruGTYwwdE0z5pkjIo-qEFXMnooAAsgfAALgStlR3F8xKzcD4Qg9BA",
    "CQACAgQAAxkBAAPWaru7ON_QWDLwmS-93vZPcCuNM1oAAsUfAALgStlRJY8N1wm23aw9BA",
    "CQACAgQAAxkBAAPYaru7SKiNPiRutLhM68YsgFgWzLsAAiIdAAJ_qNFR3k7L0rz0BB89BA",
    "CQACAgQAAxkBAAPbaru7dW9oyNhA4svxPZ2h3Q5I93IAAu8fAAIhUJhRmX43AAGr-hTdPQQ",
    "CQACAgQAAxkBAAPdaru7hUvtWeAE23gevcyIjCcRHKwAAggdAAJ_qNFRxtUBSvO3SVg9BA",
    "CQACAgQAAxkBAAPfaru7pkN4JjMX_I-ne2yJyI0lVcYAAuQfAAKPCLhRxsq5U3yKZaY9BA",
]


@router.inline_query(F.query == "audio")
async def audio(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in audiolar:
        results.append(
            types.InlineQueryResultCachedAudio(
                id=str(i),
                audio_file_id=file_id,
                caption=f"BU audio {i}"
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)