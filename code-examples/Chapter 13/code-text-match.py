import re

# Text data containing email addresses
text = "To know more about the Regular Expression you can reach to author(s) at gaurav.arora@mail.com or sachin.gupta@mail.com."

# Define a search pattern for matching email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Search for email addresses in the text
matches = re.findall(pattern, text)

# Print the matched email addresses
print("\n\tAuthor(s) email addresses:\n")
for match in matches:
    print("\t",match)
