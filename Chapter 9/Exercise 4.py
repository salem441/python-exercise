# Exercise 4: Add code to the above program to figure out who has sent the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how
# many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
file = open("mbox-short.txt")
email = {}
for line in file:
    if line.startswith('From:'):
        words = line.split()
        email_address = words[1]
        email[email_address] = email.get(email_address, 0) + 1

max_email = None
max_count = 0
for email_address, count in email.items():
    if count > max_count:
        max_email = email_address
        max_count = count

print(max_email, max_count)
