""" Te Reo Quiz, Cade Young, ......... """
import random

q_list_easy = {
  0 : {"question" : "What’s te reo Māori for ocean?", "answer" : "moana"}, 1 : {"question" : "What's te reo Māori for six?", "answer" : "ono"}, 2 : {"question" : "When would you say 'kia ora'?, when you're saying hello to someone, when you're wishing someone good health, when you're agreeing with someone or all of the above", "answer" : "all of the above"}, 3 : {"question" : "4e", "answer" : "4e"}, 4 : {"question" : "5e", "answer" : "5e"}}

q_list_medium = {
  0 : {"question" : "What's the job of the macron?", "answer" : "to lengthen the vowel"}, 1 : {"question" : "What would you catch with a pā kahawai? a) pekeketua b) ika c) manu", "answer" : "2m"}, 2 : {"question" : "If you gave a donation, gift, or contribution, you would have given a...?", "answer" : "koha"}, 3 : {"question" : "4m", "answer" : "4m"}, 4 : {"question" : "What colour is the underside of the ponga frond?hiriwa, kakariki or pango ", "answer" : "hiriwa"}}

q_list_hard = {
  0 : {"question" : "What's the translation for 'hei tiki'?", "answer" : "neck pendant of human form"}, 1 : {"question" : "What would be stored in a pātaka? pukapuka, kai or waka", "answer" : "kai"}, 2 : {"question" : "What's the te reo Māori name for Rugby Union", "answer" : "hutuporo"}, 3 : {"question" : "4h", "answer" : "4h"}, 4 : {"question" : "5h", "answer" : "5h"}}


# functions go here
def check_rounds():
  while True:
    response = input("How many rounds would you like to play? ")
    round_error = "Please type a number that is more than 0 and less than equal to 5"
    if response == "":
      response = int(response)
      print(round_error)
      continue
    if response !="":
      try:
        response = int(response)

        if response <1:
          print(round_error)
          continue

        if response >5:
          print(round_error)
          continue
      except ValueError:
        print(round_error)
        continue
    return response

#Main routine goes here

print("***in this quiz you will be asked differant questions based off of Te Reo Maori.")
print("please answer the questions exactly as they are written in the question***")
print()

while True:
  difficulty = input("Would you like to play on easy, medium, or hard: ").lower()
  if difficulty == "easy":
    difficulty = "easy"
    break
  if difficulty == "medium":
    difficulty = "medium"
    break
  if difficulty == "hard":
    difficulty = "hard"
    break
  else:
    print("Please choose one of the given difficulties")
print()




score_count = 0

rounds_played = 0

random.shuffle(q_list_easy)
random.shuffle(q_list_medium)
random.shuffle(q_list_hard)

rounds = check_rounds()

answer_setup = (q_list_easy[rounds_played], q_list_medium[rounds_played], q_list_hard[rounds_played])

end_game = "no"
while end_game == "no":
  print()

  heading = "Round {} of {}".format(rounds_played + 1, rounds)
  print(heading)
  if difficulty == "easy" or difficulty == "e":
    print(q_list_easy[rounds_played]['question'])
  if difficulty == "medium" or difficulty == "m":
    print(q_list_medium[rounds_played]['question'])
  if difficulty == "hard" or difficulty == "h":
    print(q_list_hard[rounds_played]['question'])
  choose = input("Type your answer or 'xxx' to end: ").lower()



  # rest of loop / game
  print("you chose {}".format(choose))

  if difficulty == "easy":
    if choose == q_list_easy[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer, your score is {}".format(score_count))
    if choose != q_list_easy[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_easy[rounds_played]['answer']))
        print("Your score is {}".format(score_count))
    rounds_played += 1


  if difficulty == "medium":
    if choose == q_list_medium[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer, your score is {}".format(score_count))
    if choose != q_list_medium[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_medium[rounds_played]['answer']))
        print("Your score is {}".format(score_count))
    rounds_played += 1


  if difficulty == "hard":
    if choose == q_list_hard[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer, your score is {}".format(score_count))
    if choose != q_list_hard[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_hard[rounds_played]['answer']))
        print("Your score is {}".format(score_count))
    rounds_played += 1

  if rounds_played == rounds:
    break