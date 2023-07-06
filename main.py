# Capstone-Project-1

# Questions dict

questions= [
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

# function that takes in 1 question
def ask_question(question):
    # asks user the question and stores it.
    print(question['question'])
    for option in question['options']:
        print(option)

    user_answer = input("Enter your answer (A, B, C, or D): ")
    
    # checks if correct answer
    if user_answer.upper() == question['correct_answer']:
        print('correct answer')
        # adds true in answer list
        answers.append(True)
    else:
        print('incorrect')
        # adds false in answer list
        answers.append(False)

# Loop over question in questions array 
# and each time call ask_question function with corresponing question as paremeter
for question in questions:
    ask_question(question)


print(answers)