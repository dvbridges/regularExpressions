import re


# Special sequences are predefined character classes

# \d = [0-9]
match = re.search(r"\d", "Finds the number 42")
print("Find the first number: " + match.group())

# \D = [^0-9] - i.e., not \d
match = re.search(r"\D", "Dont find the number 42")
print("Find the first non-number: " + match.group())

# \s = [\t\n\r\f\v]  - any whitespace char
match = re.search(r"\s", "lookingforthe whitespace")
print("Find the first whitespace: " + match.group())

# \S = [^\t\n\r\f\v]  - any non-whitespace char
match = re.search(r"\S", "lookingforthe whitespace")
print("Find the first non-whitespace: " + match.group())

# \w = [a-zA-Z0-9_] match any alphanumeric char
match = re.search(r"\w", "Anything but stuff like .,<>")
print("Finds first alphanumeric: " + match.group())

# \W = [^a-zA-Z0-9_] completement of \w
match = re.search(r"\W", "Noteverythingbutthingslike<>.,")
print("Finds first non-alphanumeric: " + match.group())

# \b empty strings at start or end of word
match = re.search(r"\b", "  this space before")
print("Finds first empty string: " + match.group())

# \B empty strings not at start or end of word
match = re.search(r"\B", "  this space before")
print("Finds first empty string not at start end: " + match.group())

# \\ Find the backslash
match = re.search(r"\\", "this\\that")
print("Finds first backslash: " + match.group())
