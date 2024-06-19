import re

# Text containing email addresses
text = """
Regular expressions, often abbreviated as regex or regexp, 
are powerful tools for pattern matching and text manipulation in computer science and software engineering.
Email: gaurav.arora@mail.com
Regular expressions are widely used in various fields, including text processing, data validation, and string manipulation.
Email: sachin.gupta@mail.com
"""

# Regular expression pattern for matching email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Print the found email addresses
print("\nThe input text contains following emails: ")
for email in emails:
    print(email)
