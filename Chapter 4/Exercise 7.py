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