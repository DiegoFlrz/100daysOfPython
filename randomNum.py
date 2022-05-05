import random 
# This imports the 'random' module that was already created by python to do the math. Makes it easier so programmers dont have to reinvent the wheel every time.

# random.randint(a,b) Random module generates random numbers. randint returns a random integer between a and b (both inclusive.)
random_integer = random.randint(1, 10) 
print(random_integer)

# creates a random floating point number between 0.0 and 1.000, non-inclusive so itll never be 1 or 0. Also doesnt take arguments to expand the range.
random_float = random.random() * 5
# to expand the range of floating point numbers past 1.0 you would have to do some arthmatic in order to increase the range
# in the example above, I multiplied by 5 which increases the range from 0.0  to 4.999999
print(random_float)


love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")