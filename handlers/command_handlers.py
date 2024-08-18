from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import yes_no_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU['commands']['/start'],
                         reply_markup=yes_no_keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['commands']['/help'],
                         reply_markup=yes_no_keyboard)
