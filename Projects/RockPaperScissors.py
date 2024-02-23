rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#HARD CALCULATION:

import random

choice_index=int(input("\n What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

choice=[rock,paper,scissors]

print(choice[choice_index])

print("\n computer chose \n")

random_index=random.randint(0,2)

print(choice[random_index])

if choice_index==random_index:
    print("\nDraw\n")
    #rocks[0]      beats    scissors[2]   loosses   paper[1]
    #scissors[2]   beats    paper[1]      looses    rock[0]
    #paper[1]      beats    rock[0]       looses    scissors[2]   


elif choice_index==rock:
    if(random_index==scissors):
        printf("\n YOU WIN !\n")
    else:
        printf("\n YOU LOOSE !\n")
    
elif choice_index==scissors:
    if(random_index==paper):
        printf("\n YOU WIN !\n")
    else:
        printf("\n YOU LOOSE !\n")


elif choice_index==paper:
    if(random_index==rock):
        printf("\n YOU WIN !\n")
    else:
        printf("\n YOU LOOSE !\n")


else:
    print("\n YOU LOOSE \n")

# # EASY CALCULATIONS:

#import random

# choice=int(input("\n What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# if choice==0:
#     print(rock)

# elif choice==1:
#     print(paper)

# elif choice==2:
#     print(scissors)

# random_choice=random.randint(0,2)

# print("computer choose:\n") 


# if random_choice==0:
#     print(rock)

# elif random_choice==1:
#     print(paper)

# elif random_choice==2:
#     print(scissors)
# if choice==random_choice:
#     print("\nDraw")

# else:
#     if choice==0:
#         if choice==0 and random_choice==1:
#             print("\nYou loose")

#         else:
#             print("/nYou win")

#     elif choice==1:
#         if choice==1 and random_choice==2:
#             print("\nYou loose")
#         else:
#             print("\nYou win")

#     else:
#         if choice==2 and random_choice==0:
#             print("\nYou loose")
#         else:
#             print("\nYou win")