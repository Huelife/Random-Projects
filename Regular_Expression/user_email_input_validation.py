#user_email_input_validation.py: Simple user input email check

import re

#email check currently doesnt check for foreign characters
email_check = r"[äöüéèA-Z0-9a-z!#\$%*/?\|\^\{\}`~&'+\-=_]+@[äöüéèA-Z0-9a-z!#\$%*/?\|\^\{\}`~&'+\-=_]+\.[a-z]{2,3}"

#loop continues until user inputs a valid email address
while True:
  try:
    user_email = input("Input a valid email. ")
  except ValueError:
    continue
  else:
    if re.search(email_check,user_email):
      print("Match!")
      break
    else:
      print("Invalid.")
      continue
