import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

class Greetings:
  def __init__(self,morning,afternoon,evening):
    self.morning = morning
    self.afternoon = afternoon
    self.evening = evening

bob = Greetings("How's the weather,","Afternoon,","Evening,")
peter = (Greetings("What's up, how's your morning so far","Good afternoon,",
        "It's a great evening,"))
anne = Greetings("How's your morning,","Good day,","Good evening,")

name_dict = {
  "bob": bob,
  "peter": peter,
  "anne": anne
}

while True:
  try:
    name = input("Choose 'bob', 'peter', or 'anne'. ").lower()
  except ValueError:
    continue
  else:    
    if name in name_dict:
      for key,value in name_dict.items():
        if name == key:
          if now.hour >= 0 and now.hour < 12:
            print(value.morning,key.title()+"!?")
          elif now.hour >= 12 and now.hour < 18:
            print(value.afternoon,key.title()+"!")
          elif now.hour >= 18 and now.hour < 24:
            print(value.evening,key.title()+"!")
          break
    else:
      print("{} is an invalid option.".format(key))
      continue
    break
