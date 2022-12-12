import re
message = "To be, or not to be, that is the question"
vovels = re.findall("[aeiouy]",message)
print(f"Message: {message}")
print(f"Number of vovels in text: {len(vovels)}")