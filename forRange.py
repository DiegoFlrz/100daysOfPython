# for number in range(1, 11, 5): the 5 is the 'c' or the 'step' count and not included in the range.
#     print(number)


total = 0 #Gives a variable to hold the value of the 'for loop' 
for number in range(1, 101): #sets a 'for loop' to search the range values we set.
    total += number #takes the empty variable we set and adds all the numbers in the range together
print(total)



total = 0
for even in range(2, 101, 2): #gives us a range up to 100, and we set the 'step' to 2 so it only checks the even numbers starting from 2.
    total += even
print(total)