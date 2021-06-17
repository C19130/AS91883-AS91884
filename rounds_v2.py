def check_rounds():
  while True:
    response = input("How many rounds: ")

    round_error = "Please type an integer that is more than 0 and less than equal to 10"
    if response != "":
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

# Main routine goes here...

rounds_played = 0
choose_instruction = "blah blah, paghsg"

#ask user for # rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":
  print()

  heading = "Round {} of "\
  "{}".format(rounds_played + 1, rounds)

  print(heading)
  choose = input("{} or 'xxx' to "
  "end: ".format(choose_instruction))

  # End game if exit code is typed
  if choose == "xxx":
    break

  # rest of loop / game
  print("you chose {}".format(choose))

  rounds_played += 1

  # end game if # of rounds have been played
  if rounds_played == rounds:
    break

print("Thank you for playing")