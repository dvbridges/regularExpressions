import re

# Optional items are declared using '?'
# However, you can also search for one of several regex patterns
# This is achieved using the '|' Or logical operator

# This example checks for multiple destinations in a string
pattern = r"Destination.*(Paris | Rome | London)"
msg = "Destination is London"
match = re.search(pattern, msg)
print(match.group())

# This example is useful for filtering emails in a list
pattern = r"(^To:|^From:) (David|Bridges)"
emails = ["To: Admin", "From: Admin", 
        "To: David", "From: Bridges"]
for email in emails:
    match = re.search(pattern, email)
    if match:
        print(match.group())

