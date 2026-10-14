# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency.
# Your program should convert all the input to lower case and only count the letters
# a-z. Your program should not count spaces, digits, punctuation, or anything other
# than the letters a-z. Find text samples from several different languages and see
# how letter frequency varies between languages. Compare your results with the
# tables at https://wikipedia.org/wiki/Letter_frequencies.
file = open("mbox-short.txt")
letter_count = {}
for line in file:
    line = line.lower()
    for char in line:
        if char >= 'a' and char <= 'z':
            letter_count[char] = letter_count.get(char, 0) + 1

letter_list = []
for letter, count in letter_count.items():
    letter_list.append((count, letter))

# Sort the list in reverse order
letter_list.sort(reverse=True)

# Print the letters in decreasing order of frequency
for count, letter in letter_list:
    print(letter, count)
