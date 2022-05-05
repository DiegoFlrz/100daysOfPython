print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))#Nested IF/ELSE statement
    if age < 12:
        print("Please pay $5.")
    elif age <= 18: #ELIF lets you catch more IF statements as needed.
        print("Please pay $7.")
    elif age <=25:
        print("Please pay $10")
    else:
        print("Please pay $12.")
else:
    print("you can NOT ride the rollercoaster!")
