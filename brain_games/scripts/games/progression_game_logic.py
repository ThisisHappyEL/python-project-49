from brain_games.scripts.rounds_logic import rounds_logic
from brain_games.scripts.utils import generate_number


def generate_game_stage():
    question = []
    question.append(generate_number(0, 10))
    question.append(generate_number(10, 20))
    step = question[1] - question[0]

    while len(question) != 10:
        question.append(question[-1] + step)
    
    random_space = generate_number(0, len(question) - 1)
    current_answer = question[random_space]
    question[random_space] = '..'

    question_str_list = [str(item) for item in question]
    return ' '.join(question_str_list), current_answer


def progression_game():
    game_description = 'What number is missing in the progression?'

    if rounds_logic(generate_game_stage, game_description) == 'Defeat':
        return