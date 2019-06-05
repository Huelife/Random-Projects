#solar_system_info.py: Random information about our 8 planets

#importing randint to randomize what gets printed
from random import randint

print("Hi! There are currently 8 planets in our solar system,"
      "\nhere are some information that I have gathered for each.")
print("")

#variables for each planet containing interesting facts
# Mercury
me0 = "Mercury: Planet closes to the Sun."
me1 = "Mercury: Has no moon."
me2 = "Mercury: Smallest planet."
me3 = "Mercury: A rotational day is 58 days, 15 hours, and 30 minutes."
me4 = "Mercury: The second hottest planet."
me5 = "Mercury: The most cratered planet."
me6 = "Mercury: Surface temperature is from -173 to 427 Celsius."
me7 = "Mercury: Is named for the Roman messenger to the gods."
me8 = "Mercury: Has organics and ice."
me9 = "Mercury: Has a very thin atmosphere."

# Venus
v0 = "Venus: Second planet closes to the Sun."
v1 = "Venus: Has no moon."
v2 = "Venus: Hottest planet."
v3 = "Venus: Atmosphere is 96% carbon dioxide and 3% nitrogen."
v4 = "Venus: A rotational day is 116 days, 18 hours, and 0 minutes."
v5 = "Venus: Rotates opposite of most other planets."
v6 = "Venus: Is referred to as the 'morning star' and 'evening star'."
v7 = "Venus: Named after the Roman goddess of love and beauty."
v8 = "v8"
v9 = "v9"

# Earth
e0 = "Earth: Third planet closes to the Sun."
e1 = "Earth: Currently, only planet known to support our definition of life."
e2 = "Earth: Has 1 moon: the Moon."
e3 = "Earth: 71% of the surface is covered in water."
e4 = "Earth: Atmosphere is 78.09% nitrogen and 20.95% oxygen."
e5 = "Earth: There are 7 continents, separated by 5 oceans."
e6 = "Earth: As of May 2019, human population is at 7.7 billion."
e7 = "e7"
e8 = "e8"
e9 = "e9"

# Mars
ma0 = "Mars: Fourth planet from the Sun."
ma1 = "Mars: Has 2 known moons: Phobos and Deimos."
ma2 = "Mars: Atmosphere is 95.3% carbon dioxide."
ma3 = "Mars: Named after the Roman god of war."
ma4 = "Mars: Has frozen water at its poles."
ma5 = "Mars: In 30-50 million years, Phobos will crash on mars or rip apart."
ma6 = "Mars: Slightly more than half the size of Earth."
ma7 = "ma7"
ma8 = "ma8"
ma9 = "ma9"

# Jupiter
j0 = "Jupiter: Fifth planet from the Sun."
j1 = "Jupiter: Has 79 known moons."
j2 = "Jupiter: Largest planet."
j3 = "Jupiter: Has 3 rings."
j4 = "Jupiter: Is a gas giant."
j5 = "Jupiter: Is 318 times the mass of Earth."
j6 = "Jupiter: Is the fastest spinning planet."
j7 = "Jupiter: Magnetic field is 14 times stronger than Earth's."
j8 = "Jupiter: Has storms."
j9 = "Jupiter: Named after the Roman god of the sky and thunder."

# Saturn
s0 = "Saturn: Sixth planet from the Sun."
s1 = "Saturn: Has 62 known moons."
s2 = "Saturn: Has 7 major rings."
s3 = "Saturn: Is a gas giant."
s4 = "Saturn: Atmosphere is 96.3% molecular hydrogen and 3.25% helium."
s5 = "Saturn: Is about 30% less dense than water."
s6 = "Saturn: Is 95 times the mass of Earth."
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
n5 = "Neptune: Is named for the Roman god of the sea."
n6 = "Neptune: Has storms."
n7 = "Neptune: Has the second largest planetary gravity."
n8 = "Neptune: Is the densest planet."
n9 = "Neptune: Takes 164.8 Earth years to orbit the Sun."

#planet tuples
mercury_tuple = (me0,me1,me2,me3,me4,me5,me6,me7,me8,me9)
mercury_check = ("mercury","me","mer","merc","mrcry","mercur")

venus_tuple = (v0,v1,v2,v3,v4,v5,v6,v7,v8,v9)
venus_check = ("venus","v","ve","ven","venu","vns")

earth_tuple = (e0,e1,e2,e3,e4,e5,e6,e7,e8,e9)
earth_check = ("earth","e","ea","ear","eart","erth")

mars_tuple = (ma0,ma1,ma2,ma3,ma4,ma5,ma6,ma7,ma8,ma9)
mars_check = ("mars","ma")

jupiter_tuple = (j0,j1,j2,j3,j4,j5,j6,j7,j8,j9)
jupiter_check = ("jupiter","j")

saturn_tuple = (s0,s1,s2,s3,s4,s5,s6,s7,s8,s9)
saturn_check = ("saturn","s")

uranus_tuple = (u0,u1,u2,u3,u4,u5,u6,u7,u8,u9)
uranus_check = ("uranus","u")

neptune_tuple = (n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
neptune_check = ("neptune","n")

#planet dictionary
planet_dict = {
  mercury_check:mercury_tuple,
  venus_check:venus_tuple,
  earth_check:earth_tuple,
  mars_check:mars_tuple,
  jupiter_check:jupiter_tuple,
  saturn_check:saturn_tuple,
  uranus_check:uranus_tuple,
  neptune_check:neptune_tuple
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
