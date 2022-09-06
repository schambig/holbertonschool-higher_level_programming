#!/usr/bin/python3
word = "Holberton"
# remember the lower bound is inclusive and the upper bound exclusive
word_first_3 = word[0:3]
word_last_2 = word[-2:]
# word_last_2 = word[7:] this also works
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
