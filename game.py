"""Load questions from txt file."""
from random import shuffle


def main():
    """Prints the shuffled options."""
    questions = load_questions()
    for question in questions:
        shuffled_options = shuffle_options(question)
        display_question(question[0], shuffled_options)


def load_questions():
    """Opens txt file and appends to a list."""
    questions = []
    file_open = open("Questions.txt", "r")
    for line in file_open:
        question = line.strip("\n").split(",")
        questions.append(question)
    file_open.close()
    return questions


def shuffle_options(question_row):
    """Returns shuffled options."""
    options = []
    for i in range(1, 4):
        options.append(question_row[i])
    shuffle(options)
    return options


def display_question(question, shuffled_options):
    """Displays a question with possible answers."""
    print("{}?\nA){}\nB){}\nC){}".format(question, shuffled_options[0], shuffled_options[1], shuffled_options[2]))
    user_answer = input(">>>> ")
    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>>> ")
        user_answer = user_answer.upper()
    return user_answer


main()
