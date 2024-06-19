import re

# Text data containing various phone numbers
text = """
Alternatively, you can reach to author(s) via:
Phone: 091-456-7890
Mobile: (456) 789-0123
Alternate: 987.654.3210
"""

# Define a regex pattern to match phone numbers
pattern = r'\b(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4}|\(\d{3}\)\s?\d{3}[-.\s]?\d{4})\b'

# Search for phone numbers in the text using the regex pattern
matches = re.findall(pattern, text)

# Print the matched phone numbers
print("\n\tAuthor(s) phone numbers:\n")
for match in matches:
    print("\t",match)
