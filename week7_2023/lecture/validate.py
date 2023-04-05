
import re
email = input("What's your email? ").strip().lower()

"""
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""

if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")