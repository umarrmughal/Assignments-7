#Exercise 1
''' Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps, 
distance walked, and calories burned. Write expressions to calculate average steps per week 
and total distance covered in a month.'''

#program

total_steps = 0
distance_walked = 0
calories_burned = 0

for i in range(3):
    steps = int(input("enter the steps:"))
    total_steps += steps
    distance = int(input("enter the distance walked:"))
    distance_walked += distance
    calories_burned += steps * 0.1

print("the total steps are: ",total_steps)
print("average step in a week: ",total_steps / 7)
print("distance walked in a month is: ",distance_walked)
print("the total calories burn are: ",calories_burned)
