# Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate
print("Pay:", pay)

# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate

print("Pay:", pay)


# Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
score = float(input("Enter score between 0.0 and 1.0: "))
if score < 0.0 or score > 1.0:
    print("Error: Score out of range")
else:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)
