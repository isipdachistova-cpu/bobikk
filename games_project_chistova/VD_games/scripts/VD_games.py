import prompt

ROUNDS_TO_WIN = 3


def play_game(get_rules, get_question_and_answer):
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    
    print(get_rules())
    
    correct_answers = 0
    
    while correct_answers < ROUNDS_TO_WIN:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
