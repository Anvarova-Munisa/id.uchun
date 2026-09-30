from aiogram import Router,types
router = Router()
ovozlar = [
    "AwACAgQAAxkBAAIBA2q7xjxXaAAB92wBvCz0C7l6Ou5wyAACfjoAAq73wFHOY_gqcE68PD0E",
    "AwACAgQAAxkBAAIBBWq7xkpvRm-BAp_FU37vmHSVeKG0AAJbKAAC4ejJUSiQpnJi0OWMPQQ",
    "AwACAgQAAxkBAAIBB2q7xlZSHWfFnfOEAbkvIJSawbh_AAKkJAAC4ejRUXrNiCuuCexRPQQ",
    "AwACAgQAAxkBAAIBCWq7xmERKB2UDI7JFuS8D-wjKJBKAALlPgAC4ejRUUQzKTifktAOPQQ",
    "AwACAgQAAxkBAAIBC2q7xm-xj8m87ohLUBQu9ANP74GnAAIWGQAC9lJoUkpJIZCFhKjCPQQ",
    "AwACAgQAAxkBAAIBDWq7xqFjK_ppxdumTdoILt9dE1bSAAJlQQAC6avxU2JV6LVVecvCPQQ",
]

@router.inline_query()
async def voice(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in ovozlar:
        results.append(
            types.InlineQueryResultCachedVoice(
                id=str(i),
                voice_file_id=file_id,
                title=f"Ovoz {i}",
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)