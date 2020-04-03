import re

# The syntax of regular expressions uses metacharacters
# which can act as placeholders for patterns
# '.' is a placeholder for any character

match = re.search(r'.at', 'Cat or rat')
print("First instance: " + match.group())  # reports first instance of pattern

# Square brackets are used to define character classes 
# The '-' metacharacter denotes range, e.g., a to z
# and case matters.

match = re.search(r'[A-Z]at', 'Cat or rat')
print("Only capitalized word: " +  match.group())   
match = re.search(r'[a-z]at', 'Cat or rat')
print("Only lowercase word: " + match.group())   

# The '^' character used in brackets negates choice
# but, ONLY when used as a prefix of the string inside brackets
match = re.search(r'[^A-Z]at', 'Cat or rat')
print("Only lowercase word: " + match.group())   

# Combine metachars to define your pattern
# The '*' metachar means match 0 or more reps of the preceding RE

# Over inclusive
match = re.search(r'.*sta', 'Become a Pythonista')
# More precisely
match = re.search(r'. [A-Za-z]*sta', 'Become a Pythonista')
print("What are you? " + match.group())


