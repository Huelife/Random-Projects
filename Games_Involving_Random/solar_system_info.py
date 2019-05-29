#solar_system_info.py: Random information about our 8 planets

#importing randint to randomize what gets printed
from random import randint

print("Hi! There are currently 8 planets in our solar system."
      "\nHere are some information that I have gathered for each.")
print("")

#variables for each planet containing interesting facts
# Mercury
me0 = "Mercury: Planet closes to the Sun."
me1 = "Mercury: Has no moon."
me2 = "Mercury: Smallest planet."
me3 = "Mercury: A rotational day is 58 days, 15 hours, and 30 minutes."
me4 = "me4"
me5 = "me5"
me6 = "me6"
me7 = "me7"
me8 = "me8"
me9 = "me9"

# Venus
v0 = "Venus: Second planet closes to the Sun."
v1 = "Venus: Has no moon."
v2 = "Venus: Hottest planet."
v3 = "Venus: Atmosphere is 96% carbon dioxide and 3% nitrogen."
v4 = "v4"
v5 = "v5"
v6 = "v6"
v7 = "v7"
v8 = "v8"
v9 = "v9"

# Earth
e0 = "Earth: Third planet closes to the Sun."
e1 = "Earth: Currently, only planet known to support our definition of life."
e2 = "Earth: Has 1 moon: the Moon."
e3 = "Earth: 71% of the surface is covered in water."
e4 = "Earth: Atmosphere is 78.09% nitrogen and 20.95% oxygen."
e5 = "e5"
e6 = "e6"
e7 = "e7"
e8 = "e8"
e9 = "e9"

# Mars
ma0 = "Mars: Fourth planet from the Sun."
ma1 = "Mars: Has 2 known moons: Phobos and Deimos."
ma2 = "Mars: Atmosphere is 95.3% carbon dioxide."
ma3 = "ma3"
ma4 = "ma4"
ma5 = "ma5"
ma6 = "ma6"
ma7 = "ma7"
ma8 = "ma8"
ma9 = "ma9"

# Jupiter
j0 = "Jupiter: Fifth planet from the Sun."
j1 = "Jupiter: Has 79 known moons."
j2 = "Jupiter: Largest planet."
j3 = "Jupiter: Has 3 rings."
j4 = "Jupiter: Is a gas giant."
j5 = "j5"
j6 = "j6"
j7 = "j7"
j8 = "j8"
j9 = "j9"

# Saturn
s0 = "Saturn: Sixth planet from the Sun."
s1 = "Saturn: Has 62 known moons."
s2 = "Saturn: Has 7 major rings."
s3 = "Saturn: Is a gas giant."
s4 = "s4"
s5 = "s5"
s6 = "s6"
s7 = "s7"
s8 = "s8"
s9 = "s9"

# Uranus
u0 = "Uranus: Seventh planet from the Sun."
u1 = "Uranus: Has 27 known moons."
u2 = "Uranus: Axis of rotation is basically on its sides."
u3 = "Uranus: Has 13 rings."
u4 = "Uranus: Is an ice giant."
u5 = "u5"
u6 = "u6"
u7 = "u7"
u8 = "u8"
u9 = "u9"

# Neptune
n0 = "Neptune: Eighth planet from the Sun."
n1 = "Neptune: Has 14 known moons."
n2 = "Neptune: Atmosphere is 80% hydrogen and 19% helium."
n3 = "Neptune: Has 6 rings."
n4 = "Neptune: Is an ice giant."
n5 = "n5"
n6 = "n6"
n7 = "n7"
n8 = "n8"
n9 = "n9"

#planet tuples
mercury_tuple = (me0,me1,me2,me3,me4,me5,me6,me7,me8,me9)
mercury_tuple2 = ("mercury","me")

venus_tuple = (v0,v1,v2,v3,v4,v5,v6,v7,v8,v9)
venus_tuple2 = ("venus","v")

earth_tuple = (e0,e1,e2,e3,e4,e5,e6,e7,e8,e9)
earth_tuple2 = ("earth","e")

mars_tuple = (ma0,ma1,ma2,ma3,ma4,ma5,ma6,ma7,ma8,ma9)
mars_tuple2 = ("mars","ma")

jupiter_tuple = (j0,j1,j2,j3,j4,j5,j6,j7,j8,j9)
jupiter_tuple2 = ("jupiter","j")

saturn_tuple = (s0,s1,s2,s3,s4,s5,s6,s7,s8,s9)
saturn_tuple2 = ("saturn","s")

uranus_tuple = (u0,u1,u2,u3,u4,u5,u6,u7,u8,u9)
uranus_tuple2 = ("uranus","u")

neptune_tuple = (n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
neptune_tuple2 = ("neptune","n")

#planet dictionary
planet_dict = {
  mercury_tuple2:mercury_tuple,
  venus_tuple2:venus_tuple,
  earth_tuple2:earth_tuple,
  mars_tuple2:mars_tuple,
  jupiter_tuple2:jupiter_tuple,
  saturn_tuple2:saturn_tuple,
  uranus_tuple2:uranus_tuple,
  neptune_tuple2:neptune_tuple
}

#while loop continues until user enters 'q'
while True:
  try:
    planet = input("Which planet would you like information on?"
                   "\nEnter 'q' to quit. ").lower()
  except ValueError:
    continue
  else:
    print("")
    roll = randint(0,9)
    if planet == "q":
      break
    elif any(planet in planet_dict for planet in planet_dict):
      for key,value in planet_dict.items():
        if planet in key:
          print(value[roll])
          print("")
    else:
      print("{} is an invalid option.".format(planet))
      print("")
    continue
