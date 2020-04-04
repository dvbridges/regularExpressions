import re

# You can add optional items to regular expressions
# to indicate they may or may not occur. Optional
# items use the '?' symbol

# Find occurances of the name David or Dave
pattern = r"Dav(e)?(id)?"
match1 = re.search(pattern, "Looking for David")
match2 = re.search(pattern, "Looking for Dave")

print(match1.group())
print(match2.group())

# Dates might be formatted in multiple ways
pattern = r"Feb(ruary)?"
match1 = re.search(pattern, "Feb 20th 2020")
match2 = re.search(pattern, "February 20th 2020")

print(match1.group())
print(match2.group())


