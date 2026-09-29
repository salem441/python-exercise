# Exercise 1: Write a program which repeatedly reads integers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# integers. If the user enters anything other than an integer, detect their mistake
# using try and except and print an error message and skip to the next integers.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

count = 0
total = 0
while True:
    user_input = input('Enter a number:')
    if user_input == 'done':
        break
    try:
        number = int(user_input)
    except ValueError:
        print('invalid input')

    total = total + number
    count = count + 1

if count == 0:
        print ('On number entered')
else:
   average = total / count 
print (total, count, average)