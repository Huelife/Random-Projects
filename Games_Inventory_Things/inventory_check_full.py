#inventory_check_full.py: Full inventory check module with multiple items

print("")
print("Let's check your inventory!")

#setting item class for attributes
class ItemStats:
  def __init__(self,name,desc,stre,agi,spd,defe,vit,res,pie,rng):
    self.name = name
    self.desc = desc
    self.stre = stre
    self.agi = agi
    self.spd = spd
    self.defe = defe
    self.vit = vit
    self.res = res
    self.pie = pie
    self.rng = rng 
    
  def __repr__(self):
    return str(self.name)
  
#setting individual item stats from inventory
bronze_sword = ItemStats("Bronze Sword","A cheap, but effective sword for "
                          "combat.","+100","+50","+50",0,0,0,0,0)
steel_sword = ItemStats("Steel Sword","A strong, sturdy sword for combat.",
                         "+150","+100","+100",0,0,0,0,0)
legendary_sword = ItemStats("Legendary Sword","A powerful sword for combat.",
                             "+300","+200","+200",0,0,0,0,0)

bronze_helmet = ItemStats("Bronze Helmet","A cheap, but effective helmet "
                           "for defense.",0,0,0,"+75","+75","+11",0,0)
steel_helmet = ItemStats("Steel Helmet","A strong, sturdy helmet for "
                          "defense.",0,0,0,"+100","+100","+35",0,0)
legendary_helmet = ItemStats("Legendary Helmet","A powerful helmet for "
                              "defense.",0,0,0,"+180","+180","+75",0,0)

bronze_armor = ItemStats("Bronze Armor","A cheap, but effective armor for "
                         "defense.",0,0,0,"+150","+150","+30",0,0)
steel_armor = ItemStats("Steel Armor","A strong, sturdy armor for defense.",
                        0,0,0,"+200","+200","+70",0,0)
legendary_armor = ItemStats("Legendary Armor","A powerful armor for defense.",
                            0,0,0,"+300","+300","+100",0,0)

bronze_shield = ItemStats("Bronze Shield","A cheap, but effective shield "
                          "for defense.",0,0,0,"+80","+80","+50",0,0)
steel_shield = ItemStats("Steel Shield","A strong, sturdy shield for "
                         "defense.",0,0,0,"+125","+125","+95",0,0)
legendary_shield = ItemStats("Legendary Shield","A powerful shield for "
                             "defense.",0,0,0,"+200","+200","+200",0,0)

bronze_gun = ItemStats("Bronze Gun","A cheap, but effective gun for combat.",
                       "+125","+55",0,0,0,0,"+100","+100")
steel_gun = ItemStats("Steel Gun","A strong, sturdy gun for combat.",
                      "+185","+85",0,0,0,0,"+200","+200")
legendary_gun = ItemStats("Legendary Gun","A powerful gun for combat.",
                          "+355","+185",0,0,0,0,"+300","+300")

cloth_boots = ItemStats(0,"+50","+50",0,0,"+5",0,0,"Cloth Boots",
                         "A cheap, but effective pair of boots for defense.")
leather_boots = ItemStats(0,"+100","+100",0,0,"+25",0,0,"Leather Boots",
                           "A strong, sturdy pair of boots for defense.")
legendary_boots = ItemStats(0,"+300","+300",0,0,"+55",0,0,"Legendary Boots",
                             "A powerful pair of boots for defense.")

cloth_gloves = ItemStats("+50","+100","+100",0,0,0,0,0,"Cloth Gloves",
                        "A cheap, but effective pair of gloves for defense.")
leather_gloves = ItemStats("+100","+150","+150",0,0,0,0,0,"Leather Gloves",
                            "A strong, sturdy pair of gloves for defense.")
legendary_gloves = ItemStats("+200","+300","+300",0,0,0,0,0,
                  "Legendary Gloves","A powerful pair of gloves for defense.")

#setting items in swords,helmets,armors,shields,guns,boots,and gloves list
swords = [bronze_sword,bronze_sword,bronze_sword,steel_sword,steel_sword,
          legendary_sword]
helmets = [bronze_helmet,bronze_helmet,bronze_helmet,steel_helmet,
           steel_helmet,legendary_helmet]
armors = [bronze_armor,bronze_armor,bronze_armor,steel_armor,steel_armor,
          legendary_armor]
shields = [bronze_shield,bronze_shield,bronze_shield,steel_shield,
           steel_shield,legendary_shield]
guns = [bronze_gun,bronze_gun,bronze_gun,steel_gun,steel_gun,legendary_gun]
boots = [cloth_boots,cloth_boots,cloth_boots,leather_boots,leather_boots,
         legendary_boots]
gloves = [cloth_gloves,cloth_gloves,cloth_gloves,leather_gloves,
          leather_gloves,legendary_gloves]

#setting items in inventory_gear tuple and inventory_gear_list tuple
inventory_gear = (swords,helmets,armors,shields,guns,boots,gloves)
inventory_gear_list = ("Swords","Helmets","Armors","Shields","Guns","Boots",
                       "Gloves")

#while loop continues until user inputs 'Quit'
while True:
  try:
    open_inventory = input("Enter 'Open Inventory' to check inventory gear "
                           "\nor 'Quit' to leave. ")
  except ValueError:
    continue
  else:
    if open_inventory == "Quit":
      break
    elif open_inventory == "Open Inventory":
      while True:
        try:
          print("Gear options:")
          for inventory_gear_list_names in inventory_gear_list:
            print(" {}".format(inventory_gear_list_names))
          check_gear = input("Enter 'Check Swords' or other gear options. "
                             "\nEnter 'Quit' to leave. ")
        except ValueError:
          continue
        else:
          if check_gear == "Quit":
            break
 
#while loop for sword stats
          elif check_gear == "Check Swords":
            while True:
              try:
                print("Sword list({}):".format(len(swords)))
                for swords_list in swords:
                  print(" {}".format(swords_list))
                check_swords_stats = input("Enter 'Check Bronze Sword' or "
                             "other sword options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing sword name, desc, stre, agi, and spd stats
                if check_swords_stats == "Quit":
                  break
                elif check_swords_stats == "Check Bronze Sword":
                  print("")
                  print("="*len(bronze_sword.desc))
                  print(bronze_sword.name)
                  print(bronze_sword.desc)
                  print("="*len(bronze_sword.desc))
                  print("Str:",bronze_sword.stre)
                  print("Agi:",bronze_sword.agi)
                  print("Spd:",bronze_sword.spd)
                  print("_"*len(bronze_sword.desc))
                  print("")
                elif check_swords_stats == "Check Steel Sword":
                  print("")
                  print("="*len(steel_sword.desc))
                  print(steel_sword.name)
                  print(steel_sword.desc)
                  print("="*len(steel_sword.desc))
                  print("Str:",steel_sword.stre)
                  print("Agi:",steel_sword.agi)
                  print("Spd:",steel_sword.spd)
                  print("_"*len(steel_sword.desc))
                  print("")
                elif check_swords_stats == "Check Legendary Sword":
                  print("")
                  print("="*len(legendary_sword.desc))
                  print(legendary_sword.name)
                  print(legendary_sword.desc)
                  print("="*len(legendary_sword.desc))
                  print("Str:",legendary_sword.stre)
                  print("Agi:",legendary_sword.agi)
                  print("Spd:",legendary_sword.spd)
                  print("_"*len(legendary_sword.desc))
                  print("")
                continue

#while loop for helmet stats                
          elif check_gear == "Check Helmets":
            while True:
              try:
                print("Helmet list({}):".format(len(helmets)))
                for helmets_list in helmets:
                  print(" {}".format(helmets_list))
                check_helmets_stats = input("Enter 'Check Bronze Helmet' or "
                            "other helmet options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing helmet name, desc, defe, vit, and res stats
                if check_helmets_stats == "Quit":
                  break
                elif check_helmets_stats == "Check Bronze Helmet":
                  print("")
                  print("="*len(bronze_helmet.desc))
                  print(bronze_helmet.name)
                  print(bronze_helmet.desc)
                  print("="*len(bronze_helmet.desc))
                  print("Def:",bronze_helmet.defe)
                  print("Vit:",bronze_helmet.vit)
                  print("Res:",bronze_helmet.res)
                  print("_"*len(bronze_helmet.desc))
                  print("")
                elif check_helmets_stats == "Check Steel Helmet":
                  print("")
                  print("="*len(steel_helmet.desc))
                  print(steel_helmet.name)
                  print(steel_helmet.desc)
                  print("="*len(steel_helmet.desc))
                  print("Def:",steel_helmet.defe)
                  print("Vit:",steel_helmet.vit)
                  print("Res:",steel_helmet.res)
                  print("_"*len(steel_helmet.desc))
                  print("")
                elif check_helmets_stats == "Check Legendary Helmet":
                  print("")
                  print("="*len(legendary_helmet.desc))
                  print(legendary_helmet.name)
                  print(legendary_helmet.desc)
                  print("="*len(legendary_helmet.desc))
                  print("Def:",legendary_helmet.defe)
                  print("Vit:",legendary_helmet.vit)
                  print("Res:",legendary_helmet.res)
                  print("_"*len(legendary_helmet.desc))
                  print("")
                continue
                
#while loop for armor stats                
          elif check_gear == "Check Armors":
            while True:
              try:
                print("Armor list({}):".format(len(armors)))
                for armors_list in armors:
                  print(" {}".format(armors_list))
                check_armors_stats = input("Enter 'Check Bronze Armor' or "
                             "other armor options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing armor name, desc, defe, vit, and res stats
                if check_armors_stats == "Quit":
                  break
                elif check_armors_stats == "Check Bronze Armor":
                  print("")
                  print("="*len(bronze_armor.desc))
                  print(bronze_armor.name)
                  print(bronze_armor.desc)
                  print("="*len(bronze_armor.desc))
                  print("Def:",bronze_armor.defe)
                  print("Vit:",bronze_armor.vit)
                  print("Res:",bronze_armor.res)
                  print("_"*len(bronze_armor.desc))
                  print("")
                elif check_armors_stats == "Check Steel Armor":
                  print("")
                  print("="*len(steel_armor.desc))
                  print(steel_armor.name)
                  print(steel_armor.desc)
                  print("="*len(steel_armor.desc))
                  print("Def:",steel_armor.defe)
                  print("Vit:",steel_armor.vit)
                  print("Res:",steel_armor.res)
                  print("_"*len(steel_armor.desc))
                  print("")
                elif check_armors_stats == "Check Legendary Armor":
                  print("")
                  print("="*len(legendary_armor.desc))
                  print(legendary_armor.name)
                  print(legendary_armor.desc)
                  print("="*len(legendary_armor.desc))
                  print("Def:",legendary_armor.defe)
                  print("Vit:",legendary_armor.vit)
                  print("Res:",legendary_armor.res)
                  print("_"*len(legendary_armor.desc))
                  print("")
                continue
                
#while loop for shield stats               
          elif check_gear == "Check Shields":
            while True:
              try:
                print("Shield list({}):".format(len(shields)))
                for shields_list in shields:
                  print(" {}".format(shields_list))
                check_shields_stats = input("Enter 'Check Bronze Shield' or "
                            "other shield options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing shield name, desc, defe, vit, and res stats
                if check_shields_stats == "Quit":
                  break
                elif check_shields_stats == "Check Bronze Shield":
                  print("")
                  print("="*len(bronze_shield.desc))
                  print(bronze_shield.name)
                  print(bronze_shield.desc)
                  print("="*len(bronze_shield.desc))
                  print("Def:",bronze_shield.defe)
                  print("Vit:",bronze_shield.vit)
                  print("Res:",bronze_shield.res)
                  print("_"*len(bronze_shield.desc))
                  print("")
                elif check_shields_stats == "Check Steel Shield":
                  print("")
                  print("="*len(steel_shield.desc))
                  print(steel_shield.name)
                  print(steel_shield.desc)
                  print("="*len(steel_shield.desc))
                  print("Def:",steel_shield.defe)
                  print("Vit:",steel_shield.vit)
                  print("Res:",steel_shield.res)
                  print("_"*len(steel_shield.desc))
                  print("")
                elif check_shields_stats == "Check Legendary Shield":
                  print("")
                  print("="*len(legendary_shield.desc))
                  print(legendary_shield.name)
                  print(legendary_shield.desc)
                  print("="*len(legendary_shield.desc))
                  print("Def:",legendary_shield.defe)
                  print("Vit:",legendary_shield.vit)
                  print("Res:",legendary_shield.res)
                  print("_"*len(legendary_shield.desc))
                  print("")
                continue
                
#while loop for gun stats                
          elif check_gear == "Check Guns":
            while True:
              try:
                print("Guns list({}):".format(len(guns)))
                for guns_list in guns:
                  print(" {}".format(guns_list))
                check_guns_stats = input("Enter 'Check Bronze Guns' or "
                            "other gun options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing gun name, desc, stre, agi, and spd stats
                if check_guns_stats == "Quit":
                  break
                elif check_guns_stats == "Check Bronze Gun":
                  print("")
                  print("="*len(bronze_gun.desc))
                  print(bronze_gun.name)
                  print(bronze_gun.desc)
                  print("="*len(bronze_gun.desc))
                  print("Str:",bronze_gun.stre)
                  print("Agi:",bronze_gun.agi)
                  print("Pie:",bronze_gun.pie)
                  print("Rng:",bronze_gun.rng)
                  print("_"*len(bronze_gun.desc))
                  print("")
                elif check_guns_stats == "Check Steel Gun":
                  print("")
                  print("="*len(steel_gun.desc))
                  print(steel_gun.name)
                  print(steel_gun.desc)
                  print("="*len(steel_gun.desc))
                  print("Str:",steel_gun.stre)
                  print("Agi:",steel_gun.agi)
                  print("Pie:",steel_gun.pie)
                  print("Rng:",steel_gun.rng)
                  print("_"*len(steel_gun.desc))
                  print("")
                elif check_guns_stats == "Check Legendary Gun":
                  print("")
                  print("="*len(legendary_gun.desc))
                  print(legendary_gun.name)
                  print(legendary_gun.desc)
                  print("="*len(legendary_gun.desc))
                  print("Str:",legendary_gun.stre)
                  print("Agi:",legendary_gun.agi)
                  print("Pie:",legendary_gun.pie)
                  print("Rng:",legendary_gun.rng)
                  print("_"*len(legendary_gun.desc))
                  print("")
                continue
                
#while loop for boots stats                
          elif check_gear == "Check Boots":
            while True:
              try:
                print("Boots list({}):".format(len(boots)))
                for boots_list in boots:
                  print(" {}".format(boots_list))
                check_boots_stats = input("Enter 'Check Cloth Boots' or "
                           "other boots options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing boots name, desc, stre, agi, and spd stats
                if check_boots_stats == "Quit":
                  break
                elif check_boots_stats == "Check Cloth Boots":
                  print("")
                  print("="*len(cloth_boots.desc))
                  print(cloth_boots.name)
                  print(cloth_boots.desc)
                  print("="*len(cloth_boots.desc))
                  print("Agi:",cloth_boots.agi)
                  print("Spd:",cloth_boots.spd)
                  print("Res:",cloth_boots.res)
                  print("_"*len(cloth_boots.desc))
                  print("")
                elif check_boots_stats == "Check Leather Boots":
                  print("")
                  print("="*len(leather_boots.desc))
                  print(leather_boots.name)
                  print(leather_boots.desc)
                  print("="*len(leather_boots.desc))
                  print("Agi:",leather_boots.agi)
                  print("Spd:",leather_boots.spd)
                  print("Res:",leather_boots.res)
                  print("_"*len(leather_boots.desc))
                  print("")
                elif check_boots_stats == "Check Legendary Boots":
                  print("")
                  print("="*len(legendary_boots.desc))
                  print(legendary_boots.name)
                  print(legendary_boots.desc)
                  print("="*len(legendary_boots.desc))
                  print("Agi:",legendary_boots.agi)
                  print("Spd:",legendary_boots.spd)
                  print("Res:",legendary_boots.res)
                  print("_"*len(legendary_boots.desc))
                  print("")
                continue
                
#while loop for gloves stats                
          elif check_gear == "Check Gloves":
            while True:
              try:
                print("Gloves list({}):".format(len(gloves)))
                for gloves_list in gloves:
                  print(" {}".format(gloves_list))
                check_gloves_stats = input("Enter 'Check Cloth Gloves' or "
                            "other gloves options.\nEnter 'Quit' to leave. ")
              except ValueError:
                continue
              else:
#printing gloves name, desc, stre, agi, and spd stats
                if check_gloves_stats == "Quit":
                  break
                elif check_gloves_stats == "Check Cloth Gloves":
                  print("")
                  print("="*len(cloth_gloves.desc))
                  print(cloth_gloves.name)
                  print(cloth_gloves.desc)
                  print("="*len(cloth_gloves.desc))
                  print("Str:",cloth_gloves.stre)
                  print("Agi:",cloth_gloves.agi)
                  print("Spd:",cloth_gloves.spd)
                  print("_"*len(cloth_gloves.desc))
                  print("")
                elif check_gloves_stats == "Check Leather Gloves":
                  print("")
                  print("="*len(leather_gloves.desc))
                  print(leather_gloves.name)
                  print(leather_gloves.desc)
                  print("="*len(leather_gloves.desc))
                  print("Str:",leather_gloves.stre)
                  print("Agi:",leather_gloves.agi)
                  print("Spd:",leather_gloves.spd)
                  print("_"*len(leather_gloves.desc))
                  print("")
                elif check_gloves_stats == "Check Legendary Gloves":
                  print("")
                  print("="*len(legendary_gloves.desc))
                  print(legendary_gloves.name)
                  print(legendary_gloves.desc)
                  print("="*len(legendary_gloves.desc))
                  print("Str:",legendary_gloves.stre)
                  print("Agi:",legendary_gloves.agi)
                  print("Spd:",legendary_gloves.spd)
                  print("_"*len(legendary_gloves.desc))
                  print("")
                continue
          continue
    continue
