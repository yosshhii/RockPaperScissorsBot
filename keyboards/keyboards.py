from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

agreement_button = KeyboardButton(text=LEXICON_RU['actions']['agreement'])
disagreement_button = KeyboardButton(text=LEXICON_RU['actions']['disagreement'])

yes_no_keyboard_builder = ReplyKeyboardBuilder()

yes_no_keyboard_builder.row(agreement_button, disagreement_button)

yes_no_keyboard: ReplyKeyboardMarkup = yes_no_keyboard_builder.as_markup(
    resize_keyboard=True,
)

paper_button = KeyboardButton(text=LEXICON_RU['game_actions']['paper'])
rock_button = KeyboardButton(text=LEXICON_RU['game_actions']['rock'])
scissors_button = KeyboardButton(text=LEXICON_RU['game_actions']['scissors'])

game_keyboard_builder = ReplyKeyboardBuilder()

game_keyboard_builder.row(paper_button, rock_button, scissors_button)

game_keyboard = game_keyboard_builder.as_markup(
    resize_keyboard=True,
)
