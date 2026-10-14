# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.
import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url)
data = response.read()
char_count = len(data)

if char_count <= 3000:
    print(data.decode(), end="")
else:
    print(data.decode()[:3000], end="")

print(f"\nTotal characters received: {char_count}")