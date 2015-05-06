# You pick two colors randomly.
# I will mix those two colors.
# And you will have a random number of pens of the color you picked.
# I will tell you how many pens you will get.

# This is a list of colors you can choose
colors = ["red", "blue", "yellow"]

# You are going to pick two random colors
import random

first_choice = random.randint(0, len(colors)-1)
second_choice = random.randint(0, len(colors)-1)

# print "Your first choice is " + colors[first_choice] +"."
# print "Your second choice is " + colors[second_choice] +"."
