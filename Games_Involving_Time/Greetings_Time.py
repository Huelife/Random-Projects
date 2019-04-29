import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

class Greetings:
  def __init__(self,morning,afternoon,evening):
    self.morning = morning
    self.afternoon = afternoon
    self.evening = evening

bob = Greetings("How's the weather,","Afternoon,","Evening,")
peter = Greetings("What's up, how's your morning so far","Good afternoon,","How's your evening,")
anne = Greetings("How's your morning,","Good day,","Good evening,")

while True:
  try:
    name = input("Choose 'Bob', 'Peter', or 'Anne'.")
  except ValueError:
    continue
  else:
    if name == "Bob":
      if now.hour >= 0 and now.hour < 12:
        print(bob.morning,name+"!?")
      elif now.hour >= 12 and now.hour < 18:
        print(bob.afternoon,name+"!")
      elif now.hour >= 18 and now.hour < 24:
        print(bob.evening,name+"!")
    elif name == "Peter":
      if now.hour >= 0 and now.hour < 12:
        print(peter.morning,name+"!?")
      elif now.hour >= 12 and now.hour < 18:
        print(peter.afternoon,name+"!")
      elif now.hour >= 18 and now.hour < 24:
        print(peter.evening,name+"!?")
    elif name == "Anne":
      if now.hour >= 0 and now.hour < 12:
        print(anne.morning,name+"!?")
      elif now.hour >= 12 and now.hour < 18:
        print(anne.afternoon,name+"!")
      elif now.hour >= 18 and now.hour < 24:
        print(anne.evening,name+"!")
    else:
      continue
    break