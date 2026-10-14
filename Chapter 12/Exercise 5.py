# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv receives
# characters (newlines and all), not lines.
import socket
url = input("Enter a URL: ")
try:
    parts = url.split("/")
    host = parts[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    mysock.send(cmd)

    data = b""
    while True:
        chunk = mysock.recv(512)
        if not chunk:
            break
        data += chunk

    # Find the end of the headers (after the first blank line)
    header_end = data.find(b'\r\n\r\n')
    if header_end != -1:
        # Display data after the headers and blank line
        print(data[header_end + 4:].decode())
    else:
        print("Could not find the end of headers.")

    mysock.close()
except Exception as e:
    print(f"Error retrieving the URL: {e}")
