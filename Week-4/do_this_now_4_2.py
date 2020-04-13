"""
Given a string called text, e.g. text = "This is a sentence"
Write a list comprehension (one line!) that produces a list of the words that have > 3 characters
print(long_words)  Should output:  ['This', 'sentence']
"""

text = "This is a sentence"
long_words = [word for word in text.split() if len(word) > 3]
print(long_words)