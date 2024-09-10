#!/usr/bin/python3
# Generate Random Numbers And Data Using The Random Module

"""
>>>>
>>>>
>>>>
>>>>
"""

import random

# Generate a random number between 0 and 1.
# 0 is inclusive, 1 is exclusive
value = random.random()
print(value)

# Generate a random number between two numbers.
value = random.uniform(1, 10)
print(value)

# Generate random integer between two number.
# Both the numbers are inclusive.
value = random.randint(1, 10)
print(value)

# Picking a random value from a list.
greetings = ['Hello', 'Hi', 'Hey', 'Howdy']
print(random.choice(greetings))

# Picking random values multiple times from a list.
colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=5)
print(results)

# Picking random values multiple times from a list by adding a weight to colors.
# Third color have less chances to be selected.
results = random.choices(colors, weights=[18, 18, 2], k=5)
print(results)

# Shuffle values in a list inplace.
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

# Select unique random cards.
# k should be always less than length of the list.
hand = random.sample(deck, k=5)
print(hand)