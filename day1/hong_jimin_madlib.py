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

# I will mix two colors you picked.
def mixing(f,s):
    result = ""
    if f == s :
        result += s
    elif f == "red" and s == "blue" or f == "blue" and s == "red":
        result += "violet"
    elif f == "blue" and s == "yellow" or f == "yellow" and s == "blue":
        result += "green"
    elif f == "red" and s == "yellow" or f == "yellow" and s == "red":
        result += "orange"
    print "You picked " + f + " and " + s + ". I mixed those two colors and got " + result + " color."

mixing(colors[first_choice], colors[second_choice])
