from aiogram import Router, types


router = Router()
videolar = [
    "BAACAgIAAxkBAAPIaru5cX3fQvH2VRR4vHbM_7P_U7wAAgGlAALMR-FJOQpaV6mBJ309BA",
    "BAACAgIAAxkBAAPKaru5wiqv4KT5rIC25kmbSfxFRMQAAgSlAALMR-FJxdHaUytxOCw9BA",
    "BAACAgIAAxkBAAPMaru5w5YUMOEc_ZPQBveOUO0QXZ0AAgWlAALMR-FJYiT08Gwuoj49BA",
    "BAACAgIAAxkBAAPOaru5xQbWwnH7m_mVLO_BF2zXB18AAgalAALMR-FJqBAtcS6CTCc9BA",
    "BAACAgIAAxkBAAPQaru6CndMH7r9xiiF8hGRVdlhLmcAAgmlAALMR-FJQ_-KOjb2KJ49BA",
    "BAACAgIAAxkBAAPSaru6Fe3ZQM8tnll3sSYs5maX6l8AAgqlAALMR-FJnNre-Eh37Vs9BA",
]


@router.inline_query()
async def video(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in videolar:
        results.append(
            types.InlineQueryResultCachedVideo(
                id=str(i),
                video_file_id=file_id,
                title=f"Video {i}",
                caption=f"bu video file {i}",
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)