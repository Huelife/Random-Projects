#importing randint to randomize what gets printed
from random import randint

print("Hi! There are currently 8 planets in our solar system. Here are some information that I have gathered for each.")
print("")

#empty variables for each planet with string values that should contain interesting facts
# Mercury
me1 = "me1"
me2 = "me2"
me3 = "me3"
me4 = "me4"
me5 = "me5"
me6 = "me6"
me7 = "me7"
me8 = "me8"
me9 = "me9"
me10 = "me10"
# Venus
v1 = "v1"
v2 = "v2"
v3 = "v3"
v4 = "v4"
v5 = "v5"
v6 = "v6"
v7 = "v7"
v8 = "v8"
v9 = "v9"
v10 = "v10"
# Earth
e1 = "e1"
e2 = "e2"
e3 = "e3"
e4 = "e4"
e5 = "e5"
e6 = "e6"
e7 = "e7"
e8 = "e8"
e9 = "e9"
e10 = "e10"
# Mars
ma1 = "ma1"
ma2 = "ma2"
ma3 = "ma3"
ma4 = "ma4"
ma5 = "ma5"
ma6 = "ma6"
ma7 = "ma7"
ma8 = "ma8"
ma9 = "ma9"
ma10 = "ma10"
# Jupiter
j1 = "j1"
j2 = "j2"
j3 = "j3"
j4 = "j4"
j5 = "j5"
j6 = "j6"
j7 = "j7"
j8 = "j8"
j9 = "j9"
j10 = "j10"
# Saturn
s1 = "s1"
s2 = "s2"
s3 = "s3"
s4 = "s4"
s5 = "s5"
s6 = "s6"
s7 = "s7"
s8 = "s8"
s9 = "s9"
s10 = "s10"
# Uranus
u1 = "u1"
u2 = "u2"
u3 = "u3"
u4 = "u4"
u5 = "u5"
u6 = "u6"
u7 = "u7"
u8 = "u8"
u9 = "u9"
u10 = "u10"
# Neptune
n1 = "n1"
n2 = "n2"
n3 = "n3"
n4 = "n4"
n5 = "n5"
n6 = "n6"
n7 = "n7"
n8 = "n8"
n9 = "n9"
n10 = "n10"

while True:
  try:
    p = input("Which planet would you like information on? Enter 'Q' to quit. ")
  except ValueError:
    continue
  else:
    print("")
    roll = randint(1,10)
    if p == "Q":
      break
    elif p in ("mercury", "MERCURY", "Mercury", "MErcury", "me", "Me"):
      if roll == 1:
        print(me1)
      elif roll == 2:
        print(me2)
      elif roll == 3:
        print(me3)
      elif roll == 4:
        print(me4)
      elif roll == 5:
        print(me5)
      elif roll == 6:
        print(me6)
      elif roll == 7:
        print(me7)
      elif roll == 8:
        print(me8)
      elif roll == 9:
        print(me9)
      elif roll == 10:
        print(me10)
      print("")
      continue
    elif p in ("venus", "VENUS", "Venus", "VEnus", "v", "V"):
      if roll == 1:
        print(v1)
      elif roll == 2:
        print(v2)
      elif roll == 3:
        print(v3)
      elif roll == 4:
        print(v4)
      elif roll == 5:
        print(v5)
      elif roll == 6:
        print(v6)
      elif roll == 7:
        print(v7)
      elif roll == 8:
        print(v8)
      elif roll == 9:
        print(v9)
      elif roll == 10:
        print(v10)
      print("")
      continue
    elif p in ("earth", "EARTH", "Earth", "EArth", "e", "E"):
      if roll == 1:
        print(e1)
      elif roll == 2:
        print(e2)
      elif roll == 3:
        print(e3)
      elif roll == 4:
        print(e4)
      elif roll == 5:
        print(e5)
      elif roll == 6:
        print(e6)
      elif roll == 7:
        print(e7)
      elif roll == 8:
        print(e8)
      elif roll == 9:
        print(e9)
      elif roll == 10:
        print(e10)
      print("")
      continue
    elif p in ("mars", "MARS", "Mars", "MArs", "ma", "Ma"):
      if roll == 1:
        print(ma1)
      elif roll == 2:
        print(ma2)
      elif roll == 3:
        print(ma3)
      elif roll == 4:
        print(ma4)
      elif roll == 5:
        print(ma5)
      elif roll == 6:
        print(ma6)
      elif roll == 7:
        print(ma7)
      elif roll == 8:
        print(ma8)
      elif roll == 9:
        print(ma9)
      elif roll == 10:
        print(ma10)
      print("")
      continue
    elif p in ("jupiter", "JUPITER", "Jupiter", "JUpiter", "j", "J"):
      if roll == 1:
        print(j1)
      elif roll == 2:
        print(j2)
      elif roll == 3:
        print(j3)
      elif roll == 4:
        print(j4)
      elif roll == 5:
        print(j5)
      elif roll == 6:
        print(j6)
      elif roll == 7:
        print(j7)
      elif roll == 8:
        print(j8)
      elif roll == 9:
        print(j9)
      elif roll == 10:
        print(j10)
      print("")
      continue
    elif p in ("saturn", "SATURN", "Saturn", "SAturn", "s", "S"):
      if roll == 1:
        print(s1)
      elif roll == 2:
        print(s2)
      elif roll == 3:
        print(s3)
      elif roll == 4:
        print(s4)
      elif roll == 5:
        print(s5)
      elif roll == 6:
        print(s6)
      elif roll == 7:
        print(s7)
      elif roll == 8:
        print(s8)
      elif roll == 9:
        print(s9)
      elif roll == 10:
        print(s10)
      print("")
      continue
    elif p in ("uranus", "URANUS", "Uranus", "URanus", "u", "U"):
      if roll == 1:
        print(u1)
      elif roll == 2:
        print(u2)
      elif roll == 3:
        print(u3)
      elif roll == 4:
        print(u4)
      elif roll == 5:
        print(u5)
      elif roll == 6:
        print(u6)
      elif roll == 7:
        print(u7)
      elif roll == 8:
        print(u8)
      elif roll == 9:
        print(u9)
      elif roll == 10:
        print(u10)
      print("")
      continue
    elif p in ("neptune", "NEPTUNE", "Neptune", "NEptune", "n", "N"):
      if roll == 1:
        print(n1)
      elif roll == 2:
        print(n2)
      elif roll == 3:
        print(n3)
      elif roll == 4:
        print(n4)
      elif roll == 5:
        print(n5)
      elif roll == 6:
        print(n6)
      elif roll == 7:
        print(n7)
      elif roll == 8:
        print(n8)
      elif roll == 9:
        print(n9)
      elif roll == 10:
        print(n10)
      print("")
      continue
    continue
