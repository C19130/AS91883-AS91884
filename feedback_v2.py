import random

question_list = {
  0 : {"question" : "What’s te reo Māori for ocean?", "answer" : "moana"}, 1 : {"question" : "true or false, the macron extends vowels", "answer" : "true"}, 2 : {"question" : "What would you catch with a pā kahawai?", "answer" : "ika"}, 3 : {"question" : "What's the translation for'hei tiki'?", "answer" : "neck pendant of human form"}, 4 : {"question" : "What would be stored in a pātaka?", "answer" : "kai"}, 5 : {"question" : "What's the Te Reo translation for six?", "answer" : "ono"}, 6 : {"question" : "If you gave a donation, gift, or contribution, you would have given a...?", "answer" : "koha"}, 7 : {"question" : "What colour is the underside of the ponga frond?", "answer" : "hiriwa"}, 8 : {"question" : "What is the Te Reo translation for rugby?", "answer" : "hutuporo"}, 9 : {"question" : "What is the Te Reo translation for green?", "answer" : "kakariki"}}

rounds_played = 0

random.shuffle(question_list)

rounds = input("How many rounds would you like to play? ")
rounds = int(rounds)

answer_setup = question_list[rounds_played]

end_game = "no"
while end_game == "no":
  print()

  heading = "Round {} of {}".format(rounds_played + 1, rounds)
  print(heading)
  print(question_list[rounds_played]['question'])
  choose = input("Type your answer or 'xxx' to end: ").lower()



  # rest of loop / game
  print("you chose {}".format(choose))
  if choose == question_list[rounds_played]['answer']:
    print("Good Job! That was the correct answer")
  if choose != question_list[rounds_played]['answer']:
    if choose == "xxx":
      break
    else:
      print("Thats incorrect, the correct answer is '{}'".format(question_list[rounds_played]['answer']))
  rounds_played += 1
  if rounds_played == rounds:
    break
  # End game if exit code is typed
