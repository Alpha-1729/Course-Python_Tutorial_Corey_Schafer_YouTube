#!/usr/bin/python3
# Regular Expression

"""
>>>> Regular Expression.
        Allow us to search for and match specific patterns of text.
>>>> Regular expression characters.
        . -> Any character except the new line.
        \d -> Digit (0-9)
        \D -> Not a digit (0-9)
        \w -> Word character (a-z, A-Z, 0-9, _)
        \W -> Not a word character.
        \s -> Whitespace (space, tab, newline)
        \S -> Not whitespace (space, tab, newline)

        # Anchors. (They dont match any characters)
        \b -> Word boundary.
            Word boundaries are indicated by whitespace or non-alphanumeric characters.
        \B -> Not a word boundary
        ^ -> Beginning of the string.
        $ -> End of the string.

        [] -> Matches characters in brackets.
        [^] -> Matches characters NOT in brackets.
>>>> Quantifiers
        Quantifiers is used to match multiple character at a time.
        * -> 0 or More
        + -> 1 or More
        ? -> 0 or One
        {3} -> Exact number.
        {3,4} -> Range of Numbers. (Minimum, Maximum)
>>>>
"""
import re

# Raw string in python.
# Raw string will interpret the string as it is.
# We will be using raw string in the regular expression.
message = r"Hello\n World"
print(message)

text_to_search  = r'''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.  ^ $ * + ? { } [ ] \ | ()

coreyms.com

321-555-4321
123.555.1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

mat
cat
bat
pat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

sentence = 'Start a sentence and then bring it to an end'

# Match a specific string.
pattern = re.compile(r'abc')

# Escaping periods.
# All the characters in the meta characters sections should be escaped.
# pattern = re.compile(r'\.')
# pattern = re.compile(r'core yms\.com')

# Searching for not digit.
# pattern = re.compile(r'\D')

# Search for a pattern with word boundary.
# pattern = re.compile(r'\bHa')

# Search for a pattern without word boundary.
# pattern = re.compile(r'\BHa')

# Search for a pattern that start with a string.
# pattern = re.compile(r'^Start')

# Search for a pattern that ends with a string.
# pattern = re.compile(r'end$')

# Match a range of characters using character set.
# pattern = re.compile(r'[1-5a-zA-z]')

# Negate everything in the character set.
# Avoid bat
# pattern = re.compile(r'[^b]at')

# Pattern to match phone numbers.
# 321-555-4321
# 123.555.1234

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# Using character set.
# All the characters in the character set are escaped by default.
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# Matching numbers start with 800 or 900
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# Matching numbers using quantifiers.
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# Pattern to match the names mentioned above.
# pattern = re.compile(r'Mr\.?\s[A-z]\w*')

# Name matching using grouping.
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# Matching email addresses mentioned above.
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# Matching urls.
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# We can use something called back reference to reference our captured group and its basically a shorthand for accessing these group indexes.
# Regular expression module has a sub method, that we can used to perform a substitution.

# Subgroup 2 and 3.
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print()

# Other methods in re module.
# findall method.
# Return the match as a list of strings.

# If it matches one group it only return the group as list.
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
print(matches)

# If it matches multiple groups, it will return all the groups as list of tuple.
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.findall(urls)
print(matches)

# If there are no groups, it will return all the matches.
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.findall(text_to_search)
print(matches)

# match method
# match will determine if the regular expression matches at the beginning of the string.
sentence = 'Start a sentence and then bring it to an end'

# This will return the index of the start of the string.
pattern = re.compile(r'Start')
match = pattern.match(sentence)
print(match)

# This will return None, since "bring" is not at the start of the sentence.
pattern = re.compile(r'bring')
match = pattern.match(sentence)
print(match)

# search method
# If we want to find matches within the entire string.
# It will print only the first match.
# It will return None if there is no match.
pattern = re.compile(r'bring')
match = pattern.search(sentence)
print(match)


# Flags in regular expression.
pattern = re.compile(r'start', re.IGNORECASE)
# Shorthand for above.
# pattern = re.compile(r'start', re.I)

match = pattern.match(sentence)
print(match)