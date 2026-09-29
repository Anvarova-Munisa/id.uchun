from aiogram import Router, types, F

router = Router()
hujjatlar = [
    "BQACAgIAAxkBAAPharu8q9Oq3njANxVrEdE0TU-yJmMAAjSlAALMR-FJLYM4UVtF6mc9BA",
    "BQACAgIAAxkBAAPjaru8t3f8nOeW64RlBeRy1spz0C8AAjWlAALMR-FJpsh6Vkx_mMQ9BA",
    "BQACAgIAAxkBAAPlaru8wT5i2h_MijyZLhlOM64QA4UAAjalAALMR-FJolcExLYV0-s9BA",
    "BQACAgIAAxkBAAPnaru8y6NZJRvAQHBETfDWq2Hn4J0AAjilAALMR-FJgv7FZ9MkzMQ9BA",
    "BQACAgIAAxkBAAPparu81uYS8YKuLNhnxzjp1n4nOggAAjmlAALMR-FJByQ2kSFIB6g9BA",
    "BQACAgIAAxkBAAPsaru88oT8G4CLee9KzbXMB3mYwIoAAjylAALMR-FJf4RoNvepaFQ9BA",
]


@router.inline_query(F.query == "document")
async def document(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in hujjatlar:
        results.append(
            types.InlineQueryResultCachedDocument(
                id=str(i),
                document_file_id=file_id,
                title=f"Hujjat {i}",
                caption=f"Hujjat {i}",
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)