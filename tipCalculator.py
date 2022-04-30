#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * .12 (12% / 100)
print("Welcome to the Tip Calculator.")
bill_total = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
bill_split = input("How many people to split the bill? (enter 1 if not splitting): ")

individual_amount = float(bill_total) / float(bill_split)
tip_converted = int(tip_percentage) / 100
total_tip = individual_amount * tip_converted
final_amount = round(individual_amount + total_tip, 2)
final_final = "{:.2f}".format(final_amount) #this line of code formats the final amount so that it looks like a normal dollar amount: ie $33.60 instead of $33.6
print(f"Each person should pay: ${final_final}")
