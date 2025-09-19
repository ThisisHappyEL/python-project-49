from brain_games.scripts.rounds_logic import rounds_logic
from brain_games.scripts.utils import generate_number


def is_odd(number: int) -> bool:
    return True if number % 2 == 0 else False


def generate_game_stage():
    question = generate_number(0, 100)
    correct_answer = is_odd(question)
    return question, 'yes' if correct_answer else 'no'


def even_game():
    game_description = ('Answer "yes" if the number is even,'
                        ' otherwise answer "no".')

    if rounds_logic(generate_game_stage, game_description) == 'Defeat':
        return
