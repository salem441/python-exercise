# Exercise 1: Download a copy of the file
# www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

# Read words from words.txt and store them as keys in a dictionary
word_dict = {}

with open("words.txt") as file:
    for line in file:
        for word in line.split():
            word_dict[word] = True


word = "python"
if word in word_dict:
    print(word, "is in the dictionary.")
else:
    print(word, "is not in the dictionary.")
