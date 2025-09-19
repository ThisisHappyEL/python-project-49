import random

from brain_games.scripts.rounds_logic import rounds_logic
from brain_games.scripts.utils import generate_number


def sign_generated() -> str:
    random_number = random.randint(1, 3)

    if (random_number == 1):
        return '-'
    elif (random_number == 2):
        return '+'
    else:
        return '*'
  

def math_result(first_int: int, operand: str, second_int: int) -> int:
    if operand == '-':
        return first_int - second_int
    if operand == '+':
        return first_int + second_int
    if operand == '*':
        return first_int * second_int


def generate_game_stage():
    first_number = generate_number(0, 10)
    second_number = generate_number(0, 10)
    sign = sign_generated()

    question = f'{first_number} {sign} {second_number}'
    correct_answer = math_result(first_number, sign, second_number)

    return question, correct_answer


def calc_game():
    game_description = 'What is the result of the expression?'

    if rounds_logic(generate_game_stage, game_description) == 'Defeat':
        return
