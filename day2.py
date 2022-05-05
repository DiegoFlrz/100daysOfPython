#num_char = len(input("What is your Name?"))
#new_num_char = str(num_char) converts the integer variable into a string data type
#print("Your name has " + new_num_char + " characters.") now that the variable is a string, it should be able to concatinate and print out the statement.

#a = 123
#print(type(a)) the TYPE function tells us what the data type of the variable is, if we get confused
#output is <class 'int'>

#a = float(123) converts the variable to a float 123.0, can also be used with str(strings) int(integers), etc
#print(type(a)) output is <class 'float'>

#print(70 + float("100.5"))floats and integers can be mathematically combined



# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
#print(type(two_digit_number)) shows me that the data type is a string
####################################
#Write your code below this line 👇
#first_digit = two_digit_number[0] subscript isolates the first(0) value of the string input. EX: 15 would be 1 and we store that in a new variable
#second_digit = two_digit_number[1] #isolates the second digit ex: 15 would be 5. you can also convert the concatinate directly into the integer ex: second_digit = int(two_digit_number[1])
# instructor combined the two integers conversions into ONE variable instead of 2 like i did. look at line 28 for teachers version
#a = int(first_digit) # converts the new ISOLATED string into an integer
#b = int(second_digit)
#print(a + b) # adds whatever the 2 digits are together.
# result = int(first_digit) + int(second_digit)
# print(result) and still get the same output as my way but its 1 line of code less so its "cleaner"
