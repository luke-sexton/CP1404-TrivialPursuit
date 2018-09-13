from random import choice


class Game:
    def __init__(self, questions, categories, score=0):
        self.questions = questions
        self.categories = categories
        self.score = score

    def play_game(self):
        while self.score < 5:
            question = self.get_question()
            user_answer = question.ask_question()
            points = question.is_correct_answer(user_answer)
            self.score += points

    def get_random_category(self):
        chosen_category = choice(self.categories)
        return chosen_category

    def get_question(self):
        category_questions = []
        category = self.get_random_category()
        for question in self.questions:
            if category == question.category:
                category_questions.append(question)
        chosen_question = choice(category_questions)
        return chosen_question
