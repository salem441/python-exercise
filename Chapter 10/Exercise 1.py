# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# 10.12. EXERCISES 129
# Enter a file name: mbox.txt
# zqian@umich.edu 195
file = open("mbox-short.txt")
email_count = {}
for line in file:
    if line.startswith('From'):
        words = line.split()
        email_address = words[1]
        email_count[email_address] = email_count.get(email_address, 0) + 1

# Create a list of (count, email) tuples
email_list = [(count, email) for email, count in email_count.items()]

# Sort the list in reverse order
email_list.sort(reverse=True)

# Print the person with the most commits
if email_list:
    max_count, max_email = email_list[0]
    print(max_email, max_count)
