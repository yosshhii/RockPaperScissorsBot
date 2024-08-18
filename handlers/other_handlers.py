from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import yes_no_keyboard

router = Router()


@router.message()
async def process_other_messages(message: Message):
    await message.answer(LEXICON_RU['other_message'],
                         reply_markup=yes_no_keyboard)

