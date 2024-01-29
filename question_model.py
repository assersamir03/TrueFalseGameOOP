import data

lenght = len(data.question_data)
theData = data.question_data


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
