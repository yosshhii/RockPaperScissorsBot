from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import game_keyboard, yes_no_keyboard

from services.services import get_winner, get_bot_choice

router = Router()


@router.message(F.text == LEXICON_RU['actions']['agreement'])
async def process_agreement(message: Message):
    await message.answer(LEXICON_RU['actions']['yes'],
                         reply_markup=game_keyboard)


@router.message(F.text == LEXICON_RU['actions']['disagreement'])
async def process_disagreement(message: Message):
    await message.answer(LEXICON_RU['actions']['no'])


@router.message(F.text.in_(LEXICON_RU['game_actions'].values()))
async def process_game_action(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(f'{LEXICON_RU['actions']['bot_choice']} - '
                         f'{LEXICON_RU['game_actions'][bot_choice]}')

    game_result = get_winner(message.text, bot_choice)
    await message.answer(LEXICON_RU['actions'][game_result],
                         reply_markup=yes_no_keyboard)
