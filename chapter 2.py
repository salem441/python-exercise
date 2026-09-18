# Write a program that uses input to prompt a user for their name
# and then welcomes them.
name = input("enter your name here\n")
welcome = "Hello " + name
print(welcome)

# Write a program to prompt the user for hours and rate per hour to
# compute gross pay.
p1 = input('Enter Hours:\n')
p2 = input('Enter Rate:\n')
Hours = float(p1)
Rate = float(p2)
pay = Hours * Rate
print(pay)

#  Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
width = 17
height = 12.0
print(width // 2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5)

# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
