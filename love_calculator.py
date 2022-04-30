# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#lower_name1 = name1.lower()
#lower_name2 = name2.lower()

#t = lower_name1.count("t") + lower_name2.count("t")
#r = lower_name1.count("r") + lower_name2.count("r")
#u = lower_name1.count("u") + lower_name2.count("u")
#e = lower_name1.count("e") + lower_name2.count("e")
#l = lower_name2.count("l") + lower_name1.count("l")
#o = lower_name2.count("o") + lower_name1.count("o")
#v = lower_name2.count("v") + lower_name1.count("v")
#e = lower_name2.count("e") + lower_name1.count("e")
#final_love = l + o + v + e
#final_true = t + r + u + e
#final_total = str(final_true) + str(final_love)
#Does not work because in order to combine the 2 variables without mathematically adding them, i converted them to strings.
#Therefore in the If/else statements I can not concatinate the string variable and the integer variables.
#if final_total <= 10 or final_total >= 90:
    #print("Your score is final_total, you go together like coke and mentos.")
#elif final_total >= 40 and final_total <= 50:
    #print("Your score is final_total, you are alright together.")
#else:
    #print("Your score is final_total.")
#Instructors solutions:
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))#This was the part i couldnt figure out, now that i see the solution, it looks so simple.
#integer_score = int(love_score)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like Coke and Mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
