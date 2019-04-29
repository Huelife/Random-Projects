print("Choose your weapon!")
print("")
weapon_list = ["Legendary Sword", "Legendary Shield", "Legendary Gun", "Legendary Bow", "Legendary Axe"]
print(weapon_list)
print("")
class Weapon_stats:
  def __init__(self,str,agi,spd,defe,vit,res,pie,rng):
    self.str = str
    self.agi = agi
    self.spd = spd
    self.defe = defe
    self.vit = vit
    self.res = res
    self.pie = pie
    self.rng = rng

legendary_sword = Weapon_stats("+100","+50","+50",0,0,0,0,0)
legendary_shield = Weapon_stats(0,0,0,"+200","+200","+200",0,0)
legendary_gun = Weapon_stats(0,"+100","+200",0,0,0,"+100",0)
legendary_bow = Weapon_stats(0,"+200","+200",0,0,0,0,"+100")
legendary_axe = Weapon_stats("+200","+25",0,0,"+50",0,0,0)

while True:
  try:
    weapon = input("Enter a number from 1-5 to see weapon name and attributes, otherwise, enter 'Quit' to leave")
  except ValueError:
    continue
  else:
    if weapon == "Quit":
      break
    elif weapon == "1":
      print ("")
      print("="*len(weapon_list[0]))
      print(weapon_list[0])
      print("="*len(weapon_list[0]))
      print("Str:",legendary_sword.str)
      print("Agi:",legendary_sword.agi)
      print("Spd:",legendary_sword.spd)
      print ("")
    elif weapon == "2":
      print ("")
      print("="*len(weapon_list[1]))
      print(weapon_list[1])
      print("="*len(weapon_list[1]))
      print("Def:",legendary_shield.defe)
      print("Vit:",legendary_shield.vit)
      print("Res:",legendary_shield.res)
      print ("")
    elif weapon == "3":
      print ("")
      print("="*len(weapon_list[2]))
      print(weapon_list[2])
      print("="*len(weapon_list[2]))
      print("Agi:",legendary_gun.agi)
      print("Spd:",legendary_gun.spd)
      print("Pie:",legendary_gun.pie)
      print ("")
    elif weapon == "4":
      print ("")
      print("="*len(weapon_list[3]))
      print(weapon_list[3])
      print("="*len(weapon_list[3]))
      print("Agi:",legendary_bow.agi)
      print("Spd:",legendary_bow.spd)
      print("Rng:",legendary_bow.rng)
      print ("")
    elif weapon == "5":
      print ("")
      print("="*len(weapon_list[4]))
      print(weapon_list[4])
      print("="*len(weapon_list[4]))
      print("Str:",legendary_axe.str)
      print("Agi:",legendary_axe.agi)
      print("Vit:",legendary_axe.vit)
      print ("")
    continue


