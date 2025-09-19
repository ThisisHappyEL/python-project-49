from brain_games.scripts.utils import generate_number
from brain_games.scripts.rounds_logic import rounds_logic

def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    number_half = number // 2
    for i in range(2, number_half):
        if number % i == 0:
            return False
    return True

def generate_game_stage():
    number = generate_number(0, 100)

    return number, 'yes' if is_prime_number(number) else 'no'


def prime_game():
    game_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    if rounds_logic(generate_game_stage, game_description) == 'Defeat':
        return
