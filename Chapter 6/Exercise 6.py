# Exercise 6: String methods
# Read the documentation of the string methods at
# https://docs.python.org/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you understand
# how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. For example, in
# find(sub[, start[, end]]), the brackets indicate optional arguments. So sub
# is required, but start is optional, and if you include start, then end is optional.

text = '  Hello, Python!  '

print(text.strip())
print(text.replace('Python', 'world'))
print(text.lower())
print(text.upper())
print(text.find('Python'))
print(text.startswith('  Hello'))   
