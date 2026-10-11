# Exercise 1: Read a file and print each line in uppercase.

filename = input("Enter a file name: ")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line.upper(), end="")

