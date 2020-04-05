import re

# Use the regex sub method to find and replace characters
# in a string

pattern = "[A-Z][a-z]+ [A-Z][a-z]+"  # Anonymize names
msg = "The name of the witnesses included Joe Bananas, and Bob Johnson."
newMsg = re.sub(pattern, "*****", msg)
print(newMsg)
