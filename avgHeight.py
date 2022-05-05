# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Code above takes the inputs and converts them all from strings to INT

#Write your code below this row 👇
total_height = 0 #creates the variable for height and gives it a value of 0
for height in student_heights:
    total_height += height #Every time this for loop runs its gonna take an item from the list and add it together.

total_students = 0 #every creates a variable to track the number of students we are checking.
for student in student_heights:
    total_students += 1 #every time the loop runs it will add a '1' counter for every item it comes across in the list.

average_height = round(total_height / total_students)
print(average_height)