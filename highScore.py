# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Code above takes the input and converts it to an integer and splits the info into a list.

#Write your code below this row 👇
highest_score = 0 #creates a new variable for us to store the 'HighScore' in
for score in student_scores:
    if score > highest_score: #for loop uses an 'if' statement to verify if the current item in the list is higher than the item value we have stored in the highest score.
        highest_score = score #sets the 'score' to highest_score if its higher than the current value
print(f"The highest score in the class is: {highest_score}") #basically the long way of using the max() function.