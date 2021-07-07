import random

question_list = ["What’s te reo Māori for ocean?", "What's the job of the macron", "What's the translation for'hei tiki'?", "What would be stored in a pātaka?", "How many kiwi are in this pikitia (picture)?", "What would you catch with a pā kahawai?", "If you gave a donation, gift, or contribution, you would have given a...?", "What colour is the underside of the ponga frond?", "What's the te reo Māori name for Rugby Union", "When would you say 'kia ora'"]

rounds_played = 0

b = "c"

while b == "b":
  random.shuffle(question_list)

rounds = input("How rounds would you like to play? ")
rounds = int(rounds)

answer_setup = question_list[rounds_played]

end_game = "no"
while end_game == "no":
  print()

  heading = "Round {} of {}".format(rounds_played + 1, rounds)
  print(heading)
  print(question_list[rounds_played])
  choose = input("Type your answer or 'xxx' to end: ").lower()
  rounds_played += 1
  # End game if exit code is typed
  if choose == "xxx":
    break

  # rest of loop / game
  print("you chose {}".format(choose))

  if rounds_played == rounds:
    break

if answer_setup == "What’s te reo Māori for ocean?":
  if choose == "moana":
    print("good")