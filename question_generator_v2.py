import random

questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

question_1 = random.choice(questions)
print(question_1)
questions.remove(question_1)
print(questions)