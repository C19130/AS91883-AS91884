import random

rounds = input("How rounds would you like to play")
rounds = int(rounds)

questions = ["What’s te reo Māori for ocean?", "What's the job of the macron", "What's the translation for'hei tiki'?", "What would be stored in a pātaka?", "How many kiwi are in this pikitia (picture)?", "What would you catch with a pā kahawai?", "If you gave a donation, gift, or contribution, you would have given a...?", "What colour is the underside of the ponga frond?", "What hākinakina (sport) is being played in this photo?", "When would you say 'kia ora'?"]


for item in range(rounds):
  question_1 = random.choice(questions)
  print(question_1)
  questions.remove(question_1)
