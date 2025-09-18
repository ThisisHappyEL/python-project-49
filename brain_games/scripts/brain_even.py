from .cli import welcome_user
import prompt
import random


def generate_number():
    return random.randint(0, 100)


def is_odd(number: int) -> str:
   return 'yes' if number % 2 == 0 else 'no'


def is_correct_answer(player_answer: str, correct_answer: str, name: str):
    if player_answer.lower() != correct_answer:
        print(f'"{player_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
        print(f"Let's try again, '{name}'!")
        return False
    else:
        print ('Correct!')
        return True


def main():

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    first_question = generate_number()
    correct_first_answer = is_odd(first_question)
    second_question = generate_number()
    correct_second_answer = is_odd(second_question)
    third_question = generate_number()
    correct_third_answer = is_odd(third_question)

    print(f'Question: {first_question}')
    first_answer = prompt.string('Your answer: ')
    if not is_correct_answer(first_answer, correct_first_answer, name):
        return

    print(f'Question: {second_question}')
    second_answer = prompt.string('Your answer: ')
    if not is_correct_answer(second_answer, correct_second_answer, name):
        return

    print(f'Question: {third_question}')
    third_answer = prompt.string('Your answer: ')
    if not is_correct_answer(third_answer, correct_third_answer, name):
        return

    print(f'Congratulations, {name}!')
