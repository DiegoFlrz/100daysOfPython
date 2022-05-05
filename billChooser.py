import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # automatically stores the split into a list called 'Names'
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names) #len() tells us the how many spots the list has so that we can call that integer later on.
random_choice = random.randint(0, length - 1) # now we can sat a random integer range from 0 to the amount of names, -1 since the computer starts counting at 0.
person_who_will_pay = names[random_choice]
print(f"Today {person_who_will_pay} will pay the bill today.")