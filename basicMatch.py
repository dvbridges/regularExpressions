import re

searchTerm = 'cat'
searchString = 'A cat and a rat can\'t be friends'

match = re.search(searchString, searchString)

# Prints the searchString with a match to searchTerm
print(match.group())


