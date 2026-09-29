from aiogram import Router, types, F

router = Router()
joylar = [
    ["sultonobod","40.657167,70.991415"],
    ["Qoqon","40.709854,71.082544"],
    ["Sultonobod2","40.656632,70.991469"],
]


@router.inline_query(F.query == "location")
async def location(query: types.InlineQuery):
    results = []
    i = 1
    for nom, lat, lon in joylar:
        results.append(
            types.InlineQueryResultLocation(
                id=str(i),
                title=f"joylashuv: {nom}",
                latitude=lat,
                longitude=lon,
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)