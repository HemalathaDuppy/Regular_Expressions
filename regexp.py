import re

# Extracting phone number
txt = "my number is 933039430511 and i will come at 5:00"
x = re.findall("\d{12}", txt)
print(x)

# First and last letter name matching
frnds = input("Enter names: ")
word = frnds.split()  # Split input into individual words

for words in word:
    # Matching the word if it starts and ends with 'a' or 'A'
    x = re.search("^a.*a$", words, re.IGNORECASE)
    if x:
        print(f"YES! The word '{words}' matches!")
    else:
        print(f"No match for the word '{words}'")
