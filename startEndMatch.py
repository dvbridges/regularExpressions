import re

# Regex can match start or end of a string
# Python uses the match method to match only to
# the beginning of a string. We will ignore match
# here, as we are interested in the cross-language
# method - to use ^ and $ for start and end matching,
# respectively

s1 = "Python is the best"
s2 = "What is the best? Python"

# Match with the start using '^'
match = re.search(r"^P[\w]*", s1)
print("Start word: " + match.group())

# Match with the end using '$'
match = re.search(r"Python$", s2)
print("End word: " + match.group())

# MULTILINE changes how search works
# Without the multiline arg, the following
# multiline string searches will fail
s1 = "Perl is good\nPython is too"
s2 = "Perl and Python\nare both languages"

# Match with the start using '^'
match = re.search(r"^Python", s1, re.MULTILINE)
print("Start word: " + match.group())

match = re.search(r"Python$", s2, re.MULTILINE)
print("End word: " + match.group())
