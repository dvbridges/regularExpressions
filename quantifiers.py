import re

# You can declare how often a pattern occurs

# '*' - the expression may repeat zero or an arbitrary number of times
pattern = r"[0-9]*$"
match = re.search(pattern, "What year is it? 2020")
print(match.group())

# Match pattern that follows a serial number like A-123-456
pattern = r"[A-Z]-[0-9]*-[0-9]*"
match = re.search(pattern, "Serial number Z-456-789")
print("Serial N: " + match.group())
match = re.search(pattern, "Serial number B-256-219")
print("Serial N: " + match.group())
match = re.search(pattern, "Phone number 02476777777")
print("No match: " + str(match))

# '+' means the expression must repeat at least once.

# Find all serial numbers starting with at least one number
pattern = r"^[0-9]+.*"  # Note, ^ indicates start str
match = re.search(pattern, "Z-456-789")
print("Z-456-789 - No match: " + str(match))
match = re.search(pattern, "1-ABC-789")
print("1-ABC-789 - match: " + match.group())

# Use curly brackets to make exact quantification

# Find all post-codes with 1 or two letters at the beginning
pattern = r"^[A-z]{1,2}[0-9]{1,2}\s*[0-9][A-z+]{2,}"  # using a comma indicates 1 or 2 patterns
codes = ["W13AW","W1 3AW","CV1 3AW", "CV13AW"]
for code in codes:
    print(re.search(pattern, code).group())


