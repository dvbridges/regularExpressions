import re

# Group patterns using round brackets

pattern = r"^([1-9]{1,2}) ([A-z]{3,10})"
dates = ["24 September",
         "1 June",
         "24 May"
        ]

# Access different groups
print("\nAccessing default numbered groups...\n")
for date in dates:
    match = re.search(pattern, date)
    print(date)
    print("Group 1: " + match.group(1))
    print("Group 2: " + match.group(2))

# Named groups
print("\nAccessing named groups...\n")
pattern = r"^(?P<day>[1-9]{1,2}) (?P<month>[A-z]{3,10})"
for date in dates:
    match = re.search(pattern, date)
    print(date)
    print("Group day: " + match.group('day'))
    print("Group month: " + match.group('month'))

