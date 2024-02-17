#problem: write a program that will mark a spot on a map with an X.


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")







# You idiot: is this you cal a code if you like this you never become programmer

# if position=="A1":
#   map[0][0]="X"
# elif position=="B1":
#   map[0][1]="X"
# elif position=="C1":
#   map[0][2]="X"
# elif position=="A2":
#   map[1][0]="X"
# elif position=="B2":
#   map[1][1]="X"
# elif position=="C2":
#   map[1][2]="X"
# elif position=="A3":
#   map[2][0]="X"
# elif position=="B3":
#   map[2][1]="X"
# elif position=="C3":
#   map[2][2]="X"
  