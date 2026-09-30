# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

maximum = None
minimum = None

while True:
    user_input = input('Enter a number:')
    if user_input == 'done':
        break
    try:
        number = int(user_input)
    except ValueError:
        print('invalid input')
       

    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number
if maximum is None:
    print('No numbers entered')
else:
    print('Maximum:', maximum)
    print('Minimum:', minimum)
