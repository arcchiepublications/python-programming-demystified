import re

# Sample text containing phone numbers in different formats
text = """
Alternatively, you can reach to author(s) via:
- Phone: 091-456-7890
- Mobile: (555) 555-5555
- Fax: 123.456.7890
"""

# Regular expression pattern to extract phone numbers
phone_pattern = r'\b(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'

# Extracting phone numbers from the text using re.findall()
phone_numbers = re.findall(phone_pattern, text)

# Printing the extracted phone numbers
print("Extracted phone numbers:")
for number in phone_numbers:
    print(number)

# Regular expression pattern to replace phone numbers with 'PHONE_NUMBER'
replacement = 'PHONE_NUMBER'
replaced_text = re.sub(phone_pattern, replacement, text)

# Printing the text with phone numbers replaced
print("\nText with phone numbers replaced:")
print(replaced_text)
