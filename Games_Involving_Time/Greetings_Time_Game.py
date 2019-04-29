#a forked and modified program from SoloLearn

#importing datetime and setting hour value to check current hour
import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

current_time = now.hour

#creating Game superclass
class Game:
  class_name = ""
  desc = ""
  objects = {}
  
  def __init__(self,name):
    self.name = name
    Game.objects[self.class_name] = self
  def get_desc(self):
    return self.desc

#creating Peter subclass
class Peter(Game):
  def __init__(self,name):
    self.class_name = "peter"
    self.time = current_time
    self._desc = "\nPeter:\nWhat's up!?"
    super().__init__(name)

#modifying and adding to Game superclass based on time of day
  @property
  def desc(self):
    if self.time == 11:
      greeting = "It's gym time!"
    elif self.time < 11 and self.time >= 0:
      greeting = "I'm tired, it's too early!"
    elif self.time > 11 and self.time <= 19:
      greeting = "Let's work!"
    elif self.time > 19 and self.time < 24:
      greeting = "Let's party!"
    return self._desc + "\n\nPeter:\n" + greeting
  @desc.setter
  def desc(self,value):
    self._desc = value

peter = Peter("Pete")

#creating Rob subclass
class Rob(Game):
  def __init__(self,name):
    self.class_name = "rob"
    self.time = current_time
    self._desc = "\nRob:\nYo!"
    super().__init__(name)

#modifying and adding to Game superclass based on time of day
  @property
  def desc(self):
    if self.time == 14:
      greeting = "Let's go climbing!"
    elif self.time < 14 and self.time >= 0:
      greeting = "It's too early!"
    elif self.time > 14 and self.time <= 19:
      greeting = "Work time!"
    elif self.time > 19 and self.time < 24:
      greeting = "Let's go bar hopping!"
    return self._desc + "\n\nRob:\n" + greeting
  @desc.setter
  def desc(self,value):
    self._desc = value

rob = Rob("Robert")

#hello function
def hello(name):
  if name in Game.objects:
    return Game.objects[name].get_desc()
  else:
    return "There's no {} here.".format(name)

#input function and splitting user input into 2 variables
def get_input():
  command = input("").split()
  speak_word = command[0]
  if speak_word in speak:
    speak_verb = speak[speak_word]
  else:
    print("Unknown command {}".format(speak_word))
    return
  if len(command) >= 2:
    name_word = command[1]
    print(speak_verb(name_word))
  else:
    print(speak_verb("nothing"))

#speak dictionairy
speak = {
  "hello": hello
}

#continuous looping of program and checking for error
#program doesnt stop without a force exit, currently
while True:
  print("")
  print("Type 'hello' and 'peter' or 'rob'")
  try:
    get_input()
  except IndexError:
    continue