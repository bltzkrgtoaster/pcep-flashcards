import random; from questions.storage import flashcardQuestions, flashcardAnswers

def start_game():
    score = 0
    question_keys = random.sample(list(flashcardQuestions.keys()), 5)
    for i, key in enumerate(question_keys, 1):
        correct_answer = flashcardAnswers[key]
        
        incorrect_keys = random.sample([k for k in flashcardAnswers if k != key], 3)
        options = [flashcardAnswers[k] for k in incorrect_keys] + [correct_answer]
        random.shuffle(options)

        print(f"\n{i}. {flashcardQuestions[key]}")
        print('\n'.join(f"  {j}) {opt}" for j, opt in enumerate(options, 1)))
        
        while True:
            try:
                user_choice = int(input('Your answer (1-4): '))
                if 1 <= user_choice <= 4: break
                print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if options[user_choice - 1] == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'Sorry, the correct answer was: {correct_answer}')
    
    print(f'\nGame over! Your score is {score}/5')

start_game()