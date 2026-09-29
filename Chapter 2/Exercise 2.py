# Write a program to prompt the user for hours and rate per hour to
# compute gross pay.
p1 = input('Enter Hours:\n')
p2 = input('Enter Rate:\n')
Hours = float(p1)
Rate = float(p2)
pay = Hours * Rate
print(pay)