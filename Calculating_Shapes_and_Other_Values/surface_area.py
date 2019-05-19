#importing decimal and pi, decimal for rounding and pi for its value
from decimal import Decimal
from math import pi

print("""Let's calculate surface area!
Please choose one of the following shapes:
'box', 'sphere', or 'pyramid'.""")
print("")

#possible inputs for box and pyramid
shape_box = ("box","bo","ox","bx")
shape_pyramid = ("pyramid","pyr","pramid","pyramd","pyrami","puramid","pyd")

#while loop continues until a shape is chosen and a float value > 0 picked
while True:
  try:
    shape = input("What shape is the object? ").lower()
  except ValueError:
    continue
  else:
    
#user can input 'box' in different formats and 'pyramid' in different formats
    if shape in shape_box or shape in shape_pyramid:
      while True:
        try:
          length = float(input("What's the length of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if length <= 0:
            print("Please input a value > 0.")
            continue
          break
      while True:
        try:
          width = float(input("What's the width of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if width <= 0:
            print("Please input a value > 0.")
            continue
          break
      while True:
        try:
          height = float(input("What's the height of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if height <= 0:
            print("Please input a value > 0.")
            continue
          break
          
#user input of height, width, and length used
#area of a box is calulated and printed
      if shape in shape_box:
        area = ((2*(height * width)) + (2*(height * length)) +
               (2*(width * length)))
        print("")
        print("The surface area of your {} is: {} units^2".format(shape,area))
          
#user input of length, width, and height is used
#area of a pyramid is calculated, rounded to 0.1 of a decimal, and printed
      elif shape in shape_pyramid:
        area = (length * width + (length % (((width / 2)*(width / 2)) +
               (height*height))) + (width % (((length / 2)*(length / 2)) +
               (height*height))))
        sarea = Decimal(str(area)).quantize(Decimal('.1'))
        print("")
        print("The surface area of your {} is: {} units^2".format(shape,sarea))
          
#user can input 'sphere' in 7 different formats
    elif shape in ("sphere","sphre","sphr","sph","spher","shere","phere"):
      while True:
        try:
          radius = float(input("What's the radius? "))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if radius <= 0:
            print("Please input a value > 0.")
            continue
          break
          
#user input of radius is used
#area of a sphere is calculated, rounded to 0.1 of a decimal and printed
      area = 4 * pi * (radius ** 2)
      sarea = Decimal(str(area)).quantize(Decimal('.1'))
      print("")
      print("The surface area of your sphere is: {} units^2".format(sarea))
      
    else:
      print("{} is not a valid input.".format(shape))
      continue
    break
