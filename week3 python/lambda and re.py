
#Extract digits from strings
import re

data = ["abc123", "hello2024", "no digits", "zip007"]

# Extract digits using regex and lambda
digits = list(map(lambda s: re.findall(r'\d+', s), data))
print(digits)  # [['123'], ['2024'], [], ['007']]


#Replace all non-alphabetic characters
import re

data = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]

# Remove all non-alphabetic characters
cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]', '', s), data))
print(cleaned)  # ['Hello', 'ABC', 'Cleantext', 'XYZ']


#Convert all email addresses to domain names


import re

emails = ["alice@gmail.com", "bob@yahoo.com", "user@outlook.com"]

# Extract domain using regex
domains = list(map(lambda s: re.search(r'@(\w+)\.com', s).group(1), emails))
print(domains)  # ['gmail', 'yahoo', 'outlook']

#Capitalize words that start with vowels
import re

words = ["apple", "banana", "orange", "grape", "umbrella"]

# Capitalize if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)', w.upper(), w), words))
print(vowel_caps)  # ['Apple', 'banana', 'Orange', 'grape', 'Umbrella']

#Replace multiple spaces with a single space

import re

texts = ["Hello   World", "Python    is great", "No extra   spaces please"]

# Normalize spaces
normalized = list(map(lambda t: re.sub(r'\s+', ' ', t), texts))
print(normalized)  # ['Hello World', 'Python is great', 'No extra spaces please'] 