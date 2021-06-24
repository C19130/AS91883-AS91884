import random

questions = ["What’s te reo Māori for ocean?", "What's the job of the macron", "What's the translation for'hei tiki'?", "What would be stored in a pātaka?", "How many kiwi are in this pikitia (picture)?", "What would you catch with a pā kahawai?", "If you gave a donation, gift, or contribution, you would have given a...?", "What colour is the underside of the ponga frond?", "What hākinakina (sport) is being played in this photo?", "When would you say 'kia ora'?"]


# functions go here

def check_rounds():
  while True:
    response = input("How many rounds would you like to play? ")
    round_error = "Please type a number that is more than 0 and less than equal to 10"
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

        if response >10:
          print(round_error)
          continue
      except ValueError:
        print(round_error)
        continue
    return response

#Main routine goes here

rounds_played = 0
choose_instruction = "Question goes here"

#ask user for # rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":
  print()

  heading = "Round {} of {}".format(rounds_played + 1, rounds)

  print(heading)
  choose = input("{} or 'xxx' to end: ".format(     ))
  rounds_played += 1
  # End game if exit code is typed
  if choose == "xxx":
    break

  # rest of loop / game
  print("you chose {}".format(choose))

  if rounds_played == rounds:
    break






print("Thank you for playing")