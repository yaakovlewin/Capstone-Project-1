# Capstone-Project-1
# Importing
import time
import threading
from os.path import exists as file_exists

# Checks to see if the file exists, if it does the program continues. if not, create the text file
if file_exists('high_score.txt'):
    pass
else:
    f = open("high_score.txt", 'w')
    f.close()


def display_welcome_message(player_name):
    print(f"Welcome, {player_name}. We hope you enjoy our quiz!\n"
          f"There are 10 questions, and you will have 10 seconds to answer each.\n"
          f"The questions have varying difficulties, with 1 point for easy, 2 for medium, and 3 for hard. Good luck!")


# Questions dict
questions = [
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['A. Mars', 'B. Saturn', 'C. Jupiter', 'D. Venus'],
        'correct_answer': 'C',
        'difficulty': 'EASY'
    },
    {
        'question': "Who plays Indiana Jones?",
        'options': ["A. Harrison Ford", "B. Tom Cruise", "C. Brad Pitt", "D. Leonardo DiCaprio"],
        'correct_answer': 'A',
        'difficulty': 'EASY'
    },
    {
        'question': "What is the name of the most northern part of mainland Britain?",
        'options': ["A. John o' Groats", "B. Land's End", "C. Loch Ness", "D. Snowdonia"],
        'correct_answer': 'A',
        'difficulty': 'EASY'
    },
    {
        'question': "What country has the highest life expectancy?",
        'options': ["A. Japan", "B. Switzerland", "C. Australia", "D. Norway"],
        'correct_answer': 'D',
        'difficulty': 'EASY'
    },
    {
        'question': "What company was originally called Cadabra?",
        'options': ["A. Amazon", "B. Google", "C. Microsoft", "D. Apple"],
        'correct_answer': 'A',
        'difficulty': 'HARD'
    },
    {
        'question': "What is the world's fastest bird?",
        'options': ["A. Peregrine Falcon", "B. Ostrich", "C. Hummingbird", "D. Swift"],
        'correct_answer': 'A',
        'difficulty': 'MEDIUM'
    },
    {
        'question': "What country has won the most World Cups?",
        'options': ["A. Brazil", "B. Germany", "C. Italy", "D. Argentina"],
        'correct_answer': 'A',
        'difficulty': 'MEDIUM'
    },
    {
        'question': "Which language has the most native speakers?",
        'options': ["A. English", "B. Italian", "C. Spanish", "D. French"],
        'correct_answer': 'C',
        'difficulty': 'HARD'
    },
    {
        'question': "Who painted the Mona Lisa?",
        'options': ["A. Leonardo da Vinci", "B. Van Gogh", "C. Michelangelo", "D. Sandro Botticelli"],
        'correct_answer': 'A',
        'difficulty': 'MEDIUM'
    },
    {
        'question': "Which planet is closest to the sun?",
        'options': ["A. Mars", "B. Uranus", "C. Earth", "D. Mercury"],
        'correct_answer': 'D',
        'difficulty': 'EASY'
    }
]

# keep track of answers in a list
answers = []
number_of_points = 0


def countdown(timer_time, timer_stop):
    print(f"You have {timer_time} seconds to answer:")
    for i in range(timer_time, -1, -1):
        if timer_stop[0]:
            break
        time.sleep(1)
    else:
        if not timer_stop[0]:
            print("Time's up!")
            timer_stop[0] = True


# Function that takes in 1 question
def ask_question(question):
    # asks user the question and stores it.
    print(question["question"])
    time.sleep(1)  # to give time for the user to read the question
    for option in question["options"]:
        print(option)

    # Timer and Timer stoper
    countdown_sec = 10
    timer_stop = [False]
    # Start timer
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
        process_answer(
            user_answer, question["correct_answer"], question["difficulty"])
    else:
        answers.append(False)
        correct_answer = question["correct_answer"]
        print(f"The correct answer is {correct_answer}")
    time.sleep(2)  # 2 second pause so the user can read the correct answer

# Answer logic


def process_answer(user_answer, correct_answer, difficulty):
    if user_answer.upper() == correct_answer:
        print("CORRECT!")
        # adds true in answer list
        answers.append(True)
        if difficulty == 'HARD':  # Points system
            global number_of_points
            number_of_points += 3
        elif difficulty == 'MEDIUM':
            number_of_points += 2
        else:
            number_of_points += 1
    else:
        # adds false in answer list
        answers.append(False)
        print("INCORRECT!")
        print(f"The correct answer is {correct_answer}")


def print_score(answers, points):
    score = sum(answers)
    print(f"You got {score}/10 correct for a score of {points}!")

# Calculating the score


def update_high_score(player_name, number_of_points, lines):
    try:  # Catches the error if there isn't a list or a file named high_score.txt
        if number_of_points >= int(lines[1]):
            print("Congratulations! You have the new high score!")
            f = open('high_score.txt', 'w')
            # Updates the text file with the new highscore
            f.writelines([f"{player_name} \n{number_of_points}"])
            f.close()
        else:
            print(
                f"{lines[0]} currently has the highest score with {lines[1]} points!")
    except:
        if not lines:  # If there is no recorded high score in the text file, the user gets the new high score
            print("Congratulations! You have the new high score!")
            f = open('high_score.txt', 'w')
            f.writelines([f"{player_name} \n{number_of_points}"])
            f.close()
        else:
            raise Exception("An error has occured. ")


def read_high_score_file():
    f = open("high_score.txt", 'r')
    # Read high_score.txt and save it as a list with name and score
    lines = f.read().splitlines()
    f.close()
    return lines


def play_quiz():
    player_name = input("Player name: ").title()
    display_welcome_message(player_name)
    input("Press enter to start!")

# For loop to ask each question in order
    for question in questions:
        ask_question(question)

    print_score(answers, number_of_points)

    lines = read_high_score_file()

    update_high_score(player_name, number_of_points, lines)


play_quiz()
