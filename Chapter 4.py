# Exercise 1: Run the program on your system and see what numbers you get. Run
# the program more than once and see what numbers you get.
# The random function is only one of many functions that handle random numbers.
# The function randint takes the parameters low and high, and returns an integer
# between low and high (including both).
# import random
# first_rand = random.randint (5, 10)
# second_rand = random.randint (5, 10)
# print (first_rand, second_rand)


# Exercise 2: Move the last line of this program to the top, so the function call
# appears before the definitions. Run the program and see what error message you
# get.

repeat_lyrics()


def print_lyrics():
    print("i am a lumberjac")
    print('I sleep all night and i work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()
# NameError: name 'print_lyrics' is not defined

# Exercise 3: Move the function call back to the bottom and move the definition
# of print_lyrics after the definition of repeat_lyrics. What happens when you
# run this program?


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("i am a lumberjac")
    print('I sleep all night and i work all day.')


repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

# Exercise 4: What is the purpose of the “def” keyword in Python?
# b) It indicates the start of a function


# Exercise 5: What will the following Python program print out?
# def fred():
# print("Zap")
# def jane():
# print("ABC")
# jane()
# fred()
# jane()

# d) ABC Zap ABC

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def comptepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        pay = hours * rate
    return pay


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

payment = comptepay(hours, rate)
print(payment)

# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


def computegrade(score):
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
    return grade


score = float(input("Enter score between 0.0 and 1.0: "))
score_grade = computegrade(score)
print(score_grade)
