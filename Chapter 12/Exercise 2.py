# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.
import socket

url = input("Enter a URL: ")
try:
    host = url.split("/")[2]
except IndexError:
    print("Invalid URL")
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host, 80))
except socket.gaierror:
    print("Error connecting to the host")
    exit()

cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

char_count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    char_count += len(data)
    if char_count <= 3000:
        print(data.decode(), end="")

mysock.close()
print(f"\nTotal characters received: {char_count}")