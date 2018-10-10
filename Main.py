from Questions import Question
from Game_Class import Game
from random import shuffle
from kivy.app import App
from kivy.app import StringProperty
from kivy.lang import Builder


class TrivialPursuitApp(App):
    question = StringProperty()
    answer_a = StringProperty()
    answer_b = StringProperty()
    answer_c = StringProperty()
    status = StringProperty()
    score = StringProperty()

    def __init__(self):
        super(TrivialPursuitApp, self).__init__()
        questions = load_questions()
        self.game = Game(questions, ["The Dark Arts", "Magical People", "Magical Objects", "Hogwarts",
                                     "Animals & Magical Creatures",
                                     "Magical Spells & Potions"])

    def build(self):
        self.title = "Harry Potter Trivial Pursuit"
        self.root = Builder.load_file('trivial_pursuit.kv')
        self.status = "Start the game by rolling the category dice."
        self.score = "Score: "
        return self.root

    def handle_category_press(self):
        category = self.game.get_random_category()
        self.root.ids.category_label.text = "Category: {}".format(category)
        self.game.current_question = self.game.get_question(category)
        self.question = self.game.current_question.question + "?"
        options = [self.game.current_question.answer, self.game.current_question.wrong_answer_1,
                   self.game.current_question.wrong_answer_2]
        shuffle(options)
        self.answer_a = options[0]
        self.answer_b = options[1]
        self.answer_c = options[2]

    def handle_answer_press(self, answer_text):
        is_correct = self.game.current_question.is_correct_answer(answer_text)
        if is_correct == 1:
            self.game.score += 1
            self.status = "Correct Answer: Roll the dice again!"
        else:
            self.status = "Incorrect Answer: Try a new question by rolling the category dice!"
        self.score = self.score + str(self.game.score)
        self.question = ""
        self.answer_a = ""
        self.answer_b = ""
        self.answer_c = ""

        # TODO then this
        # Clear the answer buttons and question label

    def add_question(self, user_question, answer, lie_1, lie_2, user_category):
        new_question = []

        if user_question == "":
            self.status = "Don't be shy, what is your question?"
        new_question.append(user_question)

        if answer == "":
            self.status = "I NEED ANSWERS!!!!"
        new_question.append(answer)
        if lie_1 == "":
            self.status = "I NEED A LIE!!!!"
        new_question.append(lie_1)
        if lie_2 == "":
            self.status = "I NEED ANOTHER LIE!!!!"
        new_question.append(lie_2)

        if user_category == "Category":
            self.status = "Don't be shy, what is your category?"
        new_question.append(user_category)

        question = Question(new_question[0], new_question[1], new_question[2], new_question[3], new_question[4])
        self.game.questions.append(question)


# def save_questions(questions):
#     question_file = open("Questions", mode="w")
#     for question in questions:
#         question_line = ",".join(question.save_to_list())
#         question_file.write(question_line + "\n")
#     question_file.close()
#
#
def load_questions():
    questions = []
    question_file = open("Questions.txt", "r")
    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(Question(question[0], question[1], question[2], question[3], question[4]))
    question_file.close()
    return questions


TrivialPursuitApp().run()
