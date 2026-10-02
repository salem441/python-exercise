# Exercise 5: Slicing strings
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
colon_index = str.find(':')

extracted_string = str[colon_index + 1:].strip()

float_value = float(extracted_string)
print(float_value) 

