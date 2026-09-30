from aiogram import Router, types

router = Router()
joylar = [
   ["Sulton obod",40.657167,70.991415],
    ["Qoqon",40.709854,71.082544],
   ["Sultonobod",40.656632,70.991469],
]


@router.inline_query()
async def location(query: types.InlineQuery):
    results = []
    i = 1
    for nom, lat, lon in joylar:
        results.append(
            types.InlineQueryResultLocation(
                id=str(i),
                title=f"Joylashuv: {nom}",
                latitude=lat,
                longitude=lon,
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)