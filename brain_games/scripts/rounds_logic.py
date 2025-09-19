from brain_games.cli import welcome_user
import prompt

def rounds_logic(generate_game_stage, game_description):
    player_name = welcome_user()
    print(game_description)

    for _ in range(3):
        question, correct_answer = generate_game_stage()

        print(f'Question {question}')
        player_answer = prompt.string('Your answer: ')

        if (player_answer == str(correct_answer)):
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {player_name}!")
            return 'Defeat'
    
    return print(f'Congratulations, {player_name}!')