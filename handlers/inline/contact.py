from aiogram import Router, types

router = Router()
kontaktlar = [
   ["ism 1 ","+998912031315"],
    ["ism 2","+998700812809"],
    ["ism 3","+998934582188"],
]


@router.inline_query()
async def contact(query: types.InlineQuery):
    results = []
    i = 1
    for ism, raqam in kontaktlar:
        results.append(
            types.InlineQueryResultContact(
                id=str(i),
                phone_number=raqam,
                first_name=f"foydalanuvci ism {i}",
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)