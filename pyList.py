import random
state_number = random.randint(0, 3)
# # lists in python look like arrays and are designated with '[]'
# # list variables are stored in ORDER, below Delaware is spot [0] meaning its the first state in the list, Pennsylvannia is in position [2] and so on.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
# # to pull data from a list:
print(states_of_america[state_number]) # call the name of the list and add the argument to '[]' to identify the index position in the list

# you can alter items in the list using similar syntax:
states_of_america[1] = "pencilvania" # this basically says that what ever is in the [1] spot, is gonna get changed to pencilvania.

#adding new items to the list:
states_of_america.append("California") # this adds new data to a list after you've created the list. Maybe theres a way to use this for user inputs or new data?

print(states_of_america)


#IndexError: List index out of range. Common error you see related to list. Usually because the top limit in the [a, b] exceeds the amount of items in a list.
# you can also nest lists in other list:
fruits = ["strawberries", "tangerines", "grapes"]
vegetables = ["kale", "tomatoes", "celery"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen [1][1])