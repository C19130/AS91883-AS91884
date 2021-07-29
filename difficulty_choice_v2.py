""" Te Reo Quiz, Cade Young, ......... """
import random

q_list_easy = {
  0 : {"question" : "1e", "answer" : "1e"}, 1 : {"question" : "2e", "answer" : "2e"}, 2 : {"question" : "3e", "answer" : "3e"}, 3 : {"question" : "4e", "answer" : "4e"}, 4 : {"question" : "5e", "answer" : "5e"}}

q_list_medium = {
  0 : {"question" : "1m", "answer" : "1m"}, 1 : {"question" : "2m", "answer" : "2m"}, 2 : {"question" : "3m", "answer" : "3m"}, 3 : {"question" : "4m", "answer" : "4m"}, 4 : {"question" : "5m", "answer" : "5m"}}

q_list_hard = {
  0 : {"question" : "1h", "answer" : "1h"}, 1 : {"question" : "2h", "answer" : "2h"}, 2 : {"question" : "3h", "answer" : "3h"}, 3 : {"question" : "4h", "answer" : "4h"}, 4 : {"question" : "5h", "answer" : "5h"}}


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

difficulty = input("Would you like to play on easy, medium, or hard: ").lower()

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