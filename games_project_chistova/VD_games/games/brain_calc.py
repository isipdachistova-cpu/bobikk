import random


def get_question_and_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    return question, str(correct_answer)


def get_game_rules():
    return "What is the result of the expression?"
