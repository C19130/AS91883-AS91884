import random

question_list = ["What’s te reo Māori for ocean?", "What's the job of the macron", "What's the translation for'hei tiki'?", "What would be stored in a pātaka?", "How many kiwi are in this pikitia (picture)?", "What would you catch with a pā kahawai?", "If you gave a donation, gift, or contribution, you would have given a...?", "What colour is the underside of the ponga frond?", "What hākinakina (sport) is being played in this photo?", "When would you say 'kia ora'?"]

def question_rand():
  question_1 = random.choice(question_list)
  print(question_1)
  question_list.remove(question_1)


print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())
print(question_rand())