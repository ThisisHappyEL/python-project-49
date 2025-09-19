from brain_games.scripts.utils import generate_number
from brain_games.scripts.rounds_logic import rounds_logic

def determinantGCD(first_number: int, second_number: int) -> int:
    most_bigger_number = first_number if first_number > second_number else second_number
    half_bigger_number = most_bigger_number // 2

    for i in range(half_bigger_number, 0, -1):
        if (first_number % i == 0 and second_number % i == 0):
            return i
        else:
            return 1
        

def generate_game_stage():
    first_number = generate_number(0, 100)
    second_number = generate_number(0, 100)

    question = f'{first_number} {second_number}'
    correct_answer = determinantGCD(first_number, second_number)

    return question, correct_answer

def gcd_game():
    game_description = 'Find the greatest common divisor of given numbers.'

    if rounds_logic(generate_game_stage, game_description) == 'Defeat':
        return