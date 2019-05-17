#importing randint to randomize what gets printed
from random import randint

print("Hi! There are currently 8 planets in our solar system. Here are some information that I have gathered for each.")
print("")
#empty variables for each planet with string values that should contain interesting facts
# Mercury
me1 = "Mercury: Planet closes to the Sun."
me2 = "Mercury: Has no moon."
me3 = "me3"
me4 = "me4"
me5 = "me5"
me6 = "me6"
me7 = "me7"
me8 = "me8"
me9 = "me9"
me10 = "me10"
# Venus
v1 = "Venus: Second planet closes to the Sun."
v2 = "Venus: Has no moon."
v3 = "v3"
v4 = "v4"
v5 = "v5"
v6 = "v6"
v7 = "v7"
v8 = "v8"
v9 = "v9"
v10 = "v10"
# Earth
e1 = "Earth: Third planet closes to the Sun."
e2 = "Earth: Currently, only planet known to support our definition of life."
e3 = "Earth: Has 1 moon: the Moon."
e4 = "e4"
e5 = "e5"
e6 = "e6"
e7 = "e7"
e8 = "e8"
e9 = "e9"
e10 = "e10"
# Mars
ma1 = "Mars: Fourth planet from the Sun."
ma2 = "Mars: Has 2 known moons: Phobos and Deimos."
ma3 = "ma3"
ma4 = "ma4"
ma5 = "ma5"
ma6 = "ma6"
ma7 = "ma7"
ma8 = "ma8"
ma9 = "ma9"
ma10 = "ma10"
# Jupiter
j1 = "Jupiter: Fifth planet from the Sun."
j2 = "Jupiter: Has 79 known moons."
j3 = "j3"
j4 = "j4"
j5 = "j5"
j6 = "j6"
j7 = "j7"
j8 = "j8"
j9 = "j9"
j10 = "j10"
# Saturn
s1 = "Saturn: Sixth planet from the Sun."
s2 = "Saturn: Has 62 known moons."
s3 = "s3"
s4 = "s4"
s5 = "s5"
s6 = "s6"
s7 = "s7"
s8 = "s8"
s9 = "s9"
s10 = "s10"
# Uranus
u1 = "Uranus: Seventh planet from the Sun."
u2 = "Uranus: Has 27 known moons."
u3 = "u3"
u4 = "u4"
u5 = "u5"
u6 = "u6"
u7 = "u7"
u8 = "u8"
u9 = "u9"
u10 = "u10"
# Neptune
n1 = "Neptune: Eigth planet from the Sun."
n2 = "Neptune: Has 14 known moons."
n3 = "n3"
n4 = "n4"
n5 = "n5"
n6 = "n6"
n7 = "n7"
n8 = "n8"
n9 = "n9"
n10 = "n10"
#planet tuples
mercury_tuple = (me1,me2,me3,me4,me5,me6,me7,me8,me9,me10)
mercury_tuple2 = ("mercury", "MERCURY", "Mercury", "MErcury", "me", "Me")
venus_tuple = (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10)
venus_tuple2 = ("venus", "VENUS", "Venus", "VEnus", "v", "V")
earth_tuple = (e1,e2,e3,e4,e5,e6,e7,e8,e9,e10)
earth_tuple2 = ("earth", "EARTH", "Earth", "EArth", "e", "E")
mars_tuple = (ma1,ma2,ma3,ma4,ma5,ma6,ma7,ma8,ma9,ma10)
mars_tuple2 = ("mars", "MARS", "Mars", "MArs", "ma", "Ma")
jupiter_tuple = (j1,j2,j3,j4,j5,j6,j7,j8,j9,j10)
jupiter_tuple2 = ("jupiter", "JUPITER", "Jupiter", "JUpiter", "j", "J")
saturn_tuple = (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
saturn_tuple2 = ("saturn", "SATURN", "Saturn", "SAturn", "s", "S")
uranus_tuple = (u1,u2,u3,u4,u5,u6,u7,u8,u9,u10)
uranus_tuple2 = ("uranus", "URANUS", "Uranus", "URanus", "u", "U")
neptune_tuple = (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
neptune_tuple2 = ("neptune", "NEPTUNE", "Neptune", "NEptune", "n", "N")
#planet dictionary
planet_dict = {
  mercury_tuple2: mercury_tuple,
  venus_tuple2: venus_tuple,
  earth_tuple2: earth_tuple,
  mars_tuple2: mars_tuple,
  jupiter_tuple2: jupiter_tuple,
  saturn_tuple2: saturn_tuple,
  uranus_tuple2: uranus_tuple,
  neptune_tuple2: neptune_tuple
}
#while loop continues until user enters 'Q'
while True:
  try:
    planet = input("Which planet would you like information on? Enter 'Q' to quit. ")
  except ValueError:
    continue
  else:
    print("")
    roll = randint(0,9)
    if planet == "Q":
      break
    for key,value in planet_dict.items():
      if planet in key:
        print(value[roll])
        print("")
    continue
