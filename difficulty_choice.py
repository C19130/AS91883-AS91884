import random

q_list_easy = {
  0 : {"question" : "1e", "answer" : "1e"}, 1 : {"question" : "2e", "answer" : "2e"}, 2 : {"question" : "3e", "answer" : "3e"}, 3 : {"question" : "4e", "answer" : "4e"}, 4 : {"question" : "5e", "answer" : "5e"}}

q_list_medium = {
  0 : {"question" : "1m", "answer" : "1m"}, 1 : {"question" : "2m", "answer" : "2m"}, 2 : {"question" : "3m", "answer" : "3m"}, 3 : {"question" : "4m", "answer" : "4m"}, 4 : {"question" : "5m", "answer" : "5m"}}

q_list_hard = {
  0 : {"question" : "1h", "answer" : "1h"}, 1 : {"question" : "2h", "answer" : "2h"}, 2 : {"question" : "3h", "answer" : "3h"}, 3 : {"question" : "4h", "answer" : "4h"}, 4 : {"question" : "5h", "answer" : "5h"}}

difficulty = input("Would you like to play on easy, medium, or hard: ").lower()



rounds_played = 0


if difficulty == "easy" or difficulty == "e":
 print(q_list_easy[rounds_played]['question'])
if difficulty == "medium" or difficulty == "m":
 print(q_list_medium[rounds_played]['question'])
if difficulty == "hard" or difficulty == "h":
 print(q_list_hard[rounds_played]['question'])