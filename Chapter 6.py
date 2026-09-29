total = 0
count = 0

while True:
    user_input = input('Enter a number: ')

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
    except ValueError:
        print('Invalid input')
        continue

    total += number
    count += 1

if count == 0:
    print('No numbers entered')
else:
    average = total / count
    print(total, count, average)
