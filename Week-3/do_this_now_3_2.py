"""
Do this now from (week 3)
Write a function to count the letters in stringI.e. count alphabetical letters, not characters
check if each char is a member (using in) of string.ascii_lowercase
Need to import string
Use char.lower() to ignore case
"""

from string import ascii_lowercase


def count_letters(string):
    """Count the Letters in string."""
    count = 0
    for character in string.lower():
        if character in ascii_lowercase:
            count += 1
    return count


name = input("Name: ")
print(count_letters(name))


# from string import ascii_lowercase
# print(ascii_lowercase)