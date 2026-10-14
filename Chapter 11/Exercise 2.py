# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.
# Enter file:mbox.txt
# 38549
# Enter file:mbox-short.txt
# 39756Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.
# Enter file:mbox.txt
# 38549
# Enter file:mbox-short.txt
# 39756
import re

filename = input("Enter file: ")
file = open(filename)

numbers = []
for line in file:
    line = line.rstrip()
    match = re.findall("New Revision: ([0-9]+)", line)
    if match:
        numbers.append(int(match[0]))

if numbers:
    average = sum(numbers) // len(numbers)
    print(average)
else:
    print("No numbers found.")
