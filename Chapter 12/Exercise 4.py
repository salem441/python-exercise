# Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
# tags from the retrieved HTML document and display the count of the paragraphs
# as the output of your program. Do not display the paragraph text, only count
# them. Test your program on several small web pages as well as some larger web
# pages.
import urllib.request
import re
url = input("Enter a URL: ")
try:
    html = urllib.request.urlopen(url).read().decode()
    tags = re.findall(r'<p>', html)
    print(f"Number of paragraph tags: {len(tags)}")
except Exception as e:
    print(f"Error retrieving the URL: {e}")
