#simple user input email check
import re

user_email_check = r"[0-9a-z]+@[a-z]+\.[a-z]{2,3}"

while True:
  try:
    user_email = input("Input a valid email. ")
  except ValueError:
    continue
  else:
    if re.search(user_email_check, user_email):
      print("Match")
    else:
      print("Invalid")
