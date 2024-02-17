import sys

def exit_program():
    sys.exit(0)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#MY METHOD:
# print("\nWelcome to Treasure Island.\n")
# print("\nYour mission is to find the treasure.\n") 
# ans1=input("\nYou're at a cross road.Where do you want to go? type "+'"left "'+"or"+'" right"\n')
# if ans1!="left":
#     print("\nYou fell into a hole.Game Over.\n")
#     exit_program()

# ans2=input("\nYou come to a lake.There is an island in the middle of the lake.Type"+'" wait "'+ " to wait for a boat. type"+'" swim "' +"to swim across.\n")
# if ans2!="wait":
#     print("\nYou Attacked by trout.Game Over.\n")
#     exit_program()

# ans3=input("\n you arrive at the island unharmed.There is a house with 3 doors.one Red,one Yellow and Blue.which colore do you choose?\n")
# if ans3=="Red":
#     print("\nBurned by fire.Game Over.\n")
#     exit_Program()

# elif ans3=="Blue":
#     print("\nEaten by beasts.Game Over.\n")
#     exit_program()

# elif ans3=="Yellow":
#     print("\nYou Win!")

# else:
#     print("\nGame Over")
#     exit_program()





#Original method:


print("\nWelcome to Treasure Island.\n")
print("\nYour mission is to find the treasure.\n")
ans1=input('\nYou\'re at a cross road.Where do you want to go? type "left" or "right"')
if ans1=="left":
    ans2=input('\nYou\'re come to a lake.There is an island in the middle of the lake.Type "wait"  to wait for a boat. type "swim" to swim across.\n')
    if ans2=="wait":
        ans3=input("\n you arrive at the island unharmed.There is a house with 3 doors.one Red,one Yellow and Blue.which colore do you choose?\n")
        if ans3=="Red":
            print("\nBurned by fire.Game Over.\n")

        elif ans3=="Blue":
            print("\nEaten by beasts.Game Over.\n")

        elif ans3=="Yellow":
            print("\nYou Win!")

        else:
            print("\nGame Over.")

    else:
        print("\nYou Attacked by trout.Game Over.\n")


else:
    print("\nYou fell into a hole.Game Over.\n")




