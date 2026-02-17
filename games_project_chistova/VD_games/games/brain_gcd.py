import random
import math


def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct_answer = math.gcd(num1, num2)
    
    question = f"{num1} {num2}"
    return question, str(correct_answer)


def get_game_rules():
    return "Find the greatest common divisor of given numbers."
