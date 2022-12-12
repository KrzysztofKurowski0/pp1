import re
message = "To be, or not to be, that is the question ala ma kota"
words = re.findall(" ",message)
print(f"Message: {message}")
print(f"Number of words in text: {len(words)+1}")