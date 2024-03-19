#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



New_letters=[]
selected_letters="" # for initilizing the selected_letters
for i in range(0,nr_letters):
    rand_letters=random.randint(0,len(letters)-1)
    New_letters.append(letters[rand_letters])
    selected_letters+=letters[rand_letters]
# print(selected_letters)

New_symbols=[]
selected_symbols=""
for i in range(0,nr_symbols):
    rand_symbols=random.randint(0,len(symbols)-1)
    New_symbols.append(symbols[rand_symbols])
    selected_symbols+=symbols[rand_symbols]
# print(selected_symbols)

New_numbers=[]
selected_numbers=""
for i in range(0,nr_numbers):
    rand_numbers=random.randint(0,len(numbers)-1)
    New_numbers.append(numbers[rand_numbers])
    selected_numbers+=numbers[rand_numbers]
# print(selected_numbers)

print(f"[EASY LEVEL] Here is your password:"+selected_letters + selected_symbols + selected_numbers)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

combined_list=New_letters+New_symbols+New_numbers
password=""
for i in range(len(combined_list)):
    rand_list=random.randint(0,len(combined_list)-1)
    password+=combined_list.pop(rand_list)

'''pop:The issue with your hard level password generation is that you're not removing
 the selected characters from "combined_list" after adding them to the "password".
 This means that the same character can be selected multiple times, leading to unexpected
   results. To fix this, you can use the "pop" method to remove the selected character 
   from "combined_list" after adding it to the "password".  '''


print(combined_list)
print(f"[HARD LEVEL] Here is your password:"+password)
#Certainly! To create a password with a random order of characters (the hard level), you can follow these steps:

#Combine the Lists: Start by combining the letters, numbers, and symbols lists into a single list. This combined list will contain all the characters you want to use in your password.

