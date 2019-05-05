from math import pi
#-----------------------Area-Volume-Super-Class------------------
class Area_Volume:
  shape_name = ""
  def __init__(self,name):
    self.name = name
#-----------------------Area-Classes-----------------------------
class Circle_Area(Area_Volume):
  def __init__(self,name,radius,area):
    self.shape_name = "circle"
    self.radius = radius
    self.area = round((pi * (radius ** 2)),1)
    super().__init__(name)

class Square_Area(Area_Volume):
  def __init__(self,name,length,width,area):
    self.shape_name = "square"
    self.length = length
    self.width = width
    self.area = length * width
    super().__init__(name)

class Triangle_Area(Area_Volume):
  def __init__(self,name,height,base,area):
    self.shape_name = "triangle"
    self.height = height
    self.base = base
    self.area = (height * base) / 2
    super().__init__(name)
#-----------------------Volume-Classes----------------------------
class Sphere_Volume(Area_Volume):
  def __init__(self,name,radius,volume):
    self.shape_name = "sphere"
    self.radius = radius
    self.volume = round(((4/3) * pi * (radius ** 3)),1)
    super().__init__(name)

class Box_Volume(Area_Volume):
  def __init__(self,name,length,width,height,volume):
    self.shape_name = "box"
    self.length = length
    self.width = width
    self.height = height
    self.volume = length * width * height
    super().__init__(name)

class Pyramid_Volume(Area_Volume):
  def __init__(self,name,length,width,height,volume):
    self.shape_name = "pyramid"
    self.length = length
    self.width = width
    self.height = height
    self.volume = round(((length * width * height) / 3),1)
    super().__init__(name)
#-----------------------Shapes-Dict-------------------------------
shapes_dict = {
  "circle": Circle_Area,
  "square": Square_Area,
  "triangle": Triangle_Area,
  "sphere": Sphere_Volume,
  "box": Box_Volume,
  "pyramid": Pyramid_Volume
}
#-----------------------while loop continues until user inputs 'q'
while True:
  try:
    user_area_volume = input("Do you want to find 'area' or 'volume'? 'q' to quit. ").lower()
  except ValueError:
    continue
  else:
    if user_area_volume == "q":
      break
#-----------------------while loop for area----------------------    
    elif user_area_volume == "area":
      while True:
        try:
          for key, value in shapes_dict.items():
            if key in ("circle","square","triangle"):
              print(*"  "+key)
          user_shape = input("Please choose a shape. 'q' to quit. ").lower()
        except ValueError:
          continue
        else:
          if user_shape in shapes_dict and user_shape == "circle":
            while True:
              try:
                radius = float(input("What's the radius? "))
              except ValueError:
                continue
              else:
                print("")
                print("Area: "+str(shapes_dict[user_shape]("",radius,"").area)+" units^2")
                print("")
              break
          elif user_shape in shapes_dict and user_shape == "square":
            while True:
              try:
                length = float(input("What's the length? "))
                width = float(input("What's the width? "))
              except ValueError:
                continue
              else:
                print("")
                print("Area: "+str(shapes_dict[user_shape]("",length,width,"").area)+" units^2")
                print("")
              break
          elif user_shape in shapes_dict and user_shape == "triangle":
            while True:
              try:
                height = float(input("What's the height? "))
                base = float(input("What's the base? "))
              except ValueError:
                continue
              else:
                print("")
                print("Area: "+str(shapes_dict[user_shape]("",height,base,"").area)+" units^2")
                print("")
              break
          elif user_shape == "q":
            break
          continue
#-----------------------while loop for volume--------------------
    elif user_area_volume == "volume":
      while True:
        try:
          for key, value in shapes_dict.items():
            if key in ("sphere","box","pyramid"):
              print(*"  "+key)
          user_shape = input("Please choose a shape. 'q' to quit. ").lower()
        except ValueError:
          continue
        else:
          if user_shape in shapes_dict and user_shape == "sphere":
            while True:
              try:
                radius = float(input("What's the radius? "))
              except ValueError:
                continue
              else:
                print("")
                print("Volume: "+str(shapes_dict[user_shape]("",radius,"").volume)+" units^3")
                print("")
              break
          elif user_shape in shapes_dict and user_shape == "box":
            while True:
              try:
                length = float(input("What's the length? "))
                width = float(input("What's the width? "))
                height = float(input("What's the height? "))
              except ValueError:
                continue
              else:
                print("")
                print("Volume: "+str(shapes_dict[user_shape]("",length,width,height,"").volume)+" units^3")
                print("")
              break
          elif user_shape in shapes_dict and user_shape == "pyramid":
            while True:
              try:
                length = float(input("What's the length? "))
                width = float(input("What's the width? "))
                height = float(input("What's the height? "))
              except ValueError:
                continue
              else:
                print("")
                print("Volume: "+str(shapes_dict[user_shape]("",length,width,height,"").volume)+" units^3")
                print("")
              break
          elif user_shape == "q":
            break
          continue
    continue
