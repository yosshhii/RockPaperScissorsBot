from random import choice

from lexicon.lexicon import LEXICON_RU


def get_bot_choice() -> str:
    return choice(list(LEXICON_RU['game_actions'].keys()))


def _normalize_user_message(user_msg):
    for key in LEXICON_RU['game_actions']:
        if LEXICON_RU['game_actions'][key] == user_msg:
            return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    rules = {
        'paper': 'scissors',
        'rock': 'paper',
        'scissors': 'rock',
    }

    user_choice = _normalize_user_message(user_choice)

    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'bot_won'
    return 'user_won'
