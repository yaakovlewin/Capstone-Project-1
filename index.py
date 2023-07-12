# Capstone-Project-1

# Importing
import time
import threading

# keep track of answers in a list
answers = []

player_name = input("Gamer name: ")
print(f"Welcome, {player_name}. Let's do some quiz!\n"
      f"We have 10 questions and you will have 10 seconds to answer each. Good luck!")

# Questions dict
questions = [
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['A. Mars', 'B. Saturn', 'C. Jupiter', 'D. Venus'],
        'correct_answer': 'C'
    },
    {
        'question': "Who plays Indiana Jones?",
        'options': ["A. Harrison Ford", "B. Tom Cruise", "C. Brad Pitt", "D. Leonardo DiCaprio"],
        'correct_answer': 'A'
    },
    {
        'question': "What is the name of the most northern part of mainland Britain?",
        'options': ["A. John o' Groats", "B. Land's End", "C. Loch Ness", "D. Snowdonia"],
        'correct_answer': 'A'
    },
    {
        'question': "What country has the highest life expectancy?",
        'options': ["A. Japan", "B. Switzerland", "C. Australia", "D. Norway"],
        'correct_answer': 'D'
    },
    {
        'question': "What company was originally called Cadabra?",
        'options': ["A. Amazon", "B. Google", "C. Microsoft", "D. Apple"],
        'correct_answer': 'A'
    },
    {
        'question': "What is the world's fastest bird?",
        'options': ["A. Peregrine Falcon", "B. Ostrich", "C. Hummingbird", "D. Swift"],
        'correct_answer': 'A'
    },
    {
        'question': "What country has won the most World Cups?",
        'options': ["A. Brazil", "B. Germany", "C. Italy", "D. Argentina"],
        'correct_answer': 'A'
    },
    {
        'question': "Which language has the more native speakers?",
        'options': ["A. English", "B. Italian", "C. Spanish", "D. French"],
        'correct_answer': 'C'
    },
    {
        'question': "Who painted the Mona Lisa??",
        'options': ["A. Leonardo da Vinci", "B. Van Gogh", "C. Michelangelo", "D. Sandro Botticelli"],
        'correct_answer': 'A'
    },
    {
        'question': "Which planet is closest to the sun?",
        'options': ["A. Mars", "B. Uranus", "C. Earth", "D. Mercury"],
        'correct_answer': 'D'
    }
]


def countdown(timer_time, timer_stop):
    for i in range(timer_time, -1, -1):
        print(f"Time: {i} sec")
        if timer_stop[0]:
            break
        time.sleep(1)
    else:
        if not timer_stop[0]:
            print("Time's up!")
            timer_stop[0] = True

# function that takes in 1 question


def ask_question(question):
    # asks user the question and stores it.
    print(question["question"])
    for option in question["options"]:
        print(option)

    # Timer
    countdown_sec = 10
    timer_stop = [False]

    timer_thread = threading.Thread(
        target=countdown, args=(countdown_sec, timer_stop))
    timer_thread.start()

    # Get user's answer
    user_answer = ''
    while user_answer == '' and not timer_stop[0]:
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    # Stop the timer and join the thread
    timer_stop[0] = True
    timer_thread.join()

    if user_answer != '':
        # check if the answer is correct
        if user_answer.upper() == question["correct_answer"]:
            print("CORRECT!")
            # adds true in answer list
            answers.append(True)
        else:
            # adds false in answer list
            answers.append(False)
            correct_answer = question["correct_answer"]
            print("INCORRECT!")
            print(f"The correct answer is {correct_answer}")


for question in questions:
    ask_question(question)

# Calculating the score
score = sum(answers)
print(f"You got {score}/10 right!")
