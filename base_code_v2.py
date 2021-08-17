""" Te Reo Quiz, Cade Young, 13/08/21, Version 5, ask the user a series of quiz questions about Te Reo Maori"""
"""Questions from MaiFM and TePapa"""

import random
import os
import time

#Easy list, version 4, store the easy questions for later use
q_list_easy = {
  0 : {"question" : "What’s te reo Māori for ocean?", "answer" : "moana"}, 1 : {"question" : "What's te reo Māori for six?", "answer" : "ono"}, 2 : {"question" : "When would you say 'kia ora'? when you're saying hello to someone, when you're wishing someone good health, when you're agreeing with someone or all of the above", "answer" : "all of the above"}, 3 : {"question" : "What's the second line of the New Zealand National Anthem?", "answer" : "o nga iwi matou ra"}, 4 : {"question" : "What is red in Te Reo Maori", "answer" : "whero"}}

#Medium list, version 4, store the medium questions for later use
q_list_medium = {
  0 : {"question" : "What's the job of the macron?", "answer" : "lengthen the vowel"}, 1 : {"question" : "What would you catch with a pā kahawai? a) pekeketua b) ika c) manu", "answer" : "ika"}, 2 : {"question" : "If you gave a donation, gift, or contribution, you would have given a...?", "answer" : "koha"}, 3 : {"question" : "what is te reo maori for silver", "answer" : "hiriwa"}, 4 : {"question" : "What colour is the underside of the ponga frond?hiriwa, kakariki or pango ", "answer" : "hiriwa"}}

#Hard list, version 4, store the hard questions for later use
q_list_hard = {
  0 : {"question" : "What's the translation for 'hei tiki'?", "answer" : "neck pendant of human form"}, 1 : {"question" : "What would be stored in a pātaka? pukapuka, kai or waka", "answer" : "kai"}, 2 : {"question" : "What's the te reo Māori name for Rugby Union", "answer" : "hutuporo"}, 3 : {"question" : "If it's Ua it is what?", "answer" : "rainy"}, 4 : {"question" : "If you were going for a hīkoi you are...", "answer" : "going for a walk"}}


# functions go here
#check_rounds, version 1, gets the user to input the number of rounds they want to play
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

#instructions, version 2, prints out the instructions
def instructions():
  print(">>>>>How To Play<<<<<")
  print("Choose the difficulty you want to play with")
  print("Choose the amount of rounds you want to play, between 1 - 5")
  print("Answer the questions exactly as they are written")
  time.sleep(5)
  os.system('clear')
  return ""

instructions()

#Difficulty, version 3, gets the user to input the difficulty he wants to play at so that the code can print out the correct questions
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

os.system('clear')


score_count = 0

rounds_played = 0

random.shuffle(q_list_easy)
random.shuffle(q_list_medium)
random.shuffle(q_list_hard)

rounds = check_rounds()

os.system('clear')

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

  #Quiz, version 4, combines the question_generator / rounds / score counter / feedback functions to quiz the user on varieing levels of questions and stores the score of the player to output at the end of the code.
  if difficulty == "easy":
    if choose == q_list_easy[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer")
      time.sleep(2)
      os.system('clear')
    if choose != q_list_easy[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_easy[rounds_played]['answer']))
        time.sleep(2)
        os.system('clear')
    rounds_played += 1


  if difficulty == "medium":
    if choose == q_list_medium[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer")
      time.sleep(2)
      os.system('clear')
    if choose != q_list_medium[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_medium[rounds_played]['answer']))
        time.sleep(2)
        os.system('clear')
    rounds_played += 1


  if difficulty == "hard":
    if choose == q_list_hard[rounds_played]['answer']:
      score_count += 1
      print("Good Job! That was the correct answer")
      time.sleep(2)
      os.system('clear')
    if choose != q_list_hard[rounds_played]['answer']:
      if choose == "xxx":
        break
      else:
        print("Thats incorrect, the correct answer is {}".format(q_list_hard[rounds_played]['answer']))
        time.sleep(2)
        os.system('clear')
    rounds_played += 1

  if rounds_played == rounds:
    break

#results, version 2, Prints out the users final score and thanks them for playing
os.system('clear')
print("Thank you for playing this quiz")
print("Your final score is {}/{}".format(score_count, rounds_played))