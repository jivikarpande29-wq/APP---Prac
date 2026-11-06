
import re

# Sample text
text = """
Contact us at jivika@gmail.com or soham@yahoo.com.
You can also email jivika123@college.edu.
For support, contact soham45@outlook.com.
"""

# Email pattern
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Find email addresses
emails = re.findall(pattern, text)

# Display email addresses
print("Email addresses found:")

for email in emails:
    print(email)

# Count total emails
print("\nTotal email addresses:", len(emails))

