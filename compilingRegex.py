import re

# If you want to reuse a regex pattern, you can compile it
# to create a regex object

# Create a postcode pattern
pattern = re.compile(r"[A-z]{1,2}[0-9]{1,2}\s?[0-9][A-z]{2}")

# Create a postcode pattern thats case-insenstive, using flags
pattern = re.compile(r"[a-z]{1,2}[0-9]{1,2}\s?[0-9][a-z]{2}", re.IGNORECASE)
postCodes = ["W13AW", "CV13AW", "What's a postcode?"]
for code in postCodes:
    print(re.search(pattern, code))
