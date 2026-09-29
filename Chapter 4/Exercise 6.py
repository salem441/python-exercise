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
