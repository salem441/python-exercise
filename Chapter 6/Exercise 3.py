# Exercise 3: Encapsulate this code in a function named count, and generalize it
# so that it accepts the string and the letter as arguments.
def count(text, letter):
    total = 0
    for character in text:
        if character == letter:
            total = total + 1
    return total

print(count('banana', 'a'))  
