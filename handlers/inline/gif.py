from aiogram import Router,types
router = Router()
giflar = [
    "CgACAgIAAxkBAAOpartxsx6FdURpYfEGXLhiSCQjbvQAAgMSAAK7alBISNoOC7V68Lw9BA",
    "CgACAgIAAxkBAAOqartxw2KOlQfIgOEJt5BPAAHFdH7uAALCFAAC__tQSA-O3z9Qq8KgPQQ",
    "CgACAgQAAxkBAAOrartxz5quFgGoVCf5oHD8OolbP-IAApgLAAJOskhQ9vfAsenhSIQ9BA",
    "CgACAgIAAxkBAAOsartx4eT3WsvqUQLAmsutR79warMAAvoTAAKu30hI-KxSIW8JvA09BA",
    "CgACAgQAAxkBAAOtartx7G70LG8ZGGMHNJuxWei97OIAAo8LAAJOskhQRU42nvoq4r09BA",
    "CgACAgIAAxkBAAOuartyAAGmr_CYtCZUTIGHnJKjMkM8AAKQFQACDX9JSEGNdj3mUBcFPQQ",
    "CgACAgQAAxkBAAOvartyFE_Ias5Eo_j7ith5CG0pbGoAAugNAALd00lQyVPrB-tTAbg9BA",
    "CgACAgQAAxkBAAOwartyHl-bP-9Y1sG___JT0BbfrKIAAsMLAAK0qklQblrQjM6JuTg9BA",
    "CgACAgQAAxkBAAOxartyJwX_HPLyYOs_iScCTBNtqY0AAoAKAAJOskhQZowicTakNH89BA",
    "CgACAgIAAxkBAAOyartyNFkrel_FtF-komW6Oa5cbiYAAjETAAJW8klIga-V8ESPt5M9BA",
    "CgACAgQAAxkBAAOzartyQfqm-FrWQmo4SpvUMXGBLmYAAmULAAJ8FFBQdJvNj8IjieA9BA",
]
@router.inline_query()
async def gif(query: types.InlineQuery):
        result = [
            types.InlineQueryResultGif(
                id = "1",
                gif_url=giflar[0],
                thumbnail_url=giflar[0],
                title="zor",
                caption="bola",
            ),
            types.InlineQueryResultGif(
                id = "2",
                gif_url=giflar[1],
                thumbnail_url=giflar[1],
            ),
            types.InlineQueryResultGif(
                id="3",
                gif_url=giflar[2],
                thumbnail_url=giflar[2],
            ),
            types.InlineQueryResultGif(
                id="4",
                gif_url=giflar[3],
                thumbnail_url=giflar[3],
            ),
            types.InlineQueryResultGif(
                id="5",
                gif_url=giflar[4],
                thumbnail_url=giflar[4],
            ),
            types.InlineQueryResultGif(
                id="6",
                gif_url=giflar[5],
                thumbnail_url=giflar[5],
            ),
        ]
        await query.answer(results=result, cache_time=1, is_personal=True)



    # await query.answer(query.gif[-1].file_id)