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
mercury_list = [me1,me2,me3,me4,me5,me6,me7,me8,me9,me10]
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
venus_list = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
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
earth_list = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
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
mars_list = [ma1,ma2,ma3,ma4,ma5,ma6,ma7,ma8,ma9,ma10]
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
jupiter_list = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10]
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
saturn_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
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
uranus_list = [u1,u2,u3,u4,u5,u6,u7,u8,u9,u10]
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
neptune_list = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
#while loop continues until user enters 'Q'
while True:
  try:
    planet = input("Which planet would you like information on? Enter 'Q' to quit. ")
  except ValueError:
    continue
  else:
    print("")
    roll = randint(1,10)
    if planet == "Q":
      break
    elif planet in ("mercury", "MERCURY", "Mercury", "MErcury", "me", "Me"):
      print(mercury_list[roll])
      print("")
    elif planet in ("venus", "VENUS", "Venus", "VEnus", "v", "V"):
      print(venus_list[roll])
      print("")
    elif planet in ("earth", "EARTH", "Earth", "EArth", "e", "E"):
      print(earth_list[roll])
      print("")
    elif planet in ("mars", "MARS", "Mars", "MArs", "ma", "Ma"):
      print(mars_list[roll])
      print("")
    elif planet in ("jupiter", "JUPITER", "Jupiter", "JUpiter", "j", "J"):
      print(jupiter_list[roll])
      print("")
    elif planet in ("saturn", "SATURN", "Saturn", "SAturn", "s", "S"):
      print(saturn_list[roll])
      print("")
    elif planet in ("uranus", "URANUS", "Uranus", "URanus", "u", "U"):
      print(uranus_list[roll])
      print("")
    elif planet in ("neptune", "NEPTUNE", "Neptune", "NEptune", "n", "N"):
      print(neptune_list[roll])
      print("")
    continue
