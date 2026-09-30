from aiogram import Router,types
router = Router()


animals = [
     "AgACAgIAAxkBAAORartrshQsGqKf6fP3F2UkUqhDkhwAAl8gaxvMR-FJqMPf1SqrYJIBAAMCAAN5AAM9BA",
      "AgACAgIAAxkBAAOTartsHsmX3uAIOP7ifyuPEicuEEEAAmIgaxvMR-FJ-WWJkOeC2p4BAAMCAAN5AAM9BA",
       "AgACAgIAAxkBAAOXartsiPSyIuCahdNtdMKRUCEhY5gAAmUgaxvMR-FJbt91iqMAAVMJAQADAgADeAADPQQ",
      "AgACAgIAAxkBAAOVartsVhRYic5352lFdZ6m7WRLw-cAAmMgaxvMR-FJ2b5OLr0uuo4BAAMCAAN5AAM9BA",
       "AgACAgIAAxkBAAOZarttA7VHrt6bQ1hoV9puG5LgarAAAmcgaxvMR-FJbwh5Bx0AAWgdAQADAgADeAADPQQ",
      "AgACAgIAAxkBAAObarttNTXkVZ1DyBv2k1xvTQG432UAAmkgaxvMR-FJEFist8D-KDUBAAMCAANtAAM9BA",
    "AgACAgIAAxkBAAOdarttSkcbsPHDwTiEq--3sX9N7yIAAmsgaxvMR-FJlcj0l1RFPwwBAAMCAAN4AAM9BA",
    "AgACAgIAAxkBAAOfarttdtK_355LSQABz5JO5EpoP2QlAAJuIGsbzEfhSQQSID92FNE0AQADAgADeAADPQQ",
    "AgACAgIAAxkBAAOharttvthbheoSAAFmSjoNdHuBQ2GCAAJyIGsbzEfhSX5Dm7uLEnLsAQADAgADeAADPQQ",
    "AgACAgIAAxkBAAOjartt0OZZU7_ojx3wB2EFSztun3IAAnQgaxvMR-FJ4igpyVDW5BcBAAMCAAN4AAM9BA",

 ]

@router.inline_query()
async def photo(query: types.InlineQuery):
        results = []
        i = 1
        for url in animals:
            results.append(
                types.InlineQueryResultPhoto(
                    id=str(i),
                    thumbnail_url=url,
                    photo_url=url,
                )
            )
            i = i + 1
        await query.answer(results=results, cache_time=1, is_personal=True)
