#Capstone-Project-1
# This is the Welcoming message
print("Welcome to our amazing quiz! Im sure you will have a great time!")
print("You will be shown a question and a choice of three answers.")
print("The only thing you need to type in is either A B or C")
name = str(input("What is your name? Please add it here: "))
print("Hello ",name,"Lets get going!")

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
        'options': ["A. Japan", "B. Switzerland", "C. Australia", "D. Hong Kong"],
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
    }

]


# keep track of answers in a list

answers = []

# tracking the score
score = 0



# function that takes in 1 question
def ask_question(question):
    global score  # Add global keyword to access the global variable inside the function

    # asks user the question and stores it.
    
    print(question['question'])
    
    for option in question['options']:

        print(option)


    user_answer = input("Enter your answer (A, B, C, or D): ")



    # checks if correct answer

    if user_answer.upper() == question['correct_answer']:

        print('correct answer')

        # adds true in answer list

        print('Correct answer')
        score += 10
        # adds True in answer list
        answers.append(True)

    else:

        print('incorrect')
        print('correct answer is: ', question['correct_answer'])

        # adds false in answer list

        print('Incorrect')
        # adds False in answer list
        answers.append(False)




# Loop over question in questions array 

# and each time call ask_question function with corresponing question as paremeter

for question in questions:

    ask_question(question)

print("That's all the questions, ", name, "! Let's see how you did!")
print("Answers:", answers)
# should print the score out at the end
print("Score:", score)