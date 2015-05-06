# You pick two colors randomly.
# And you will have a random number of pens of the color you picked.

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


# I will tell how many number of pen you will have.

min_num = int(raw_input("Enter minimum number of pen you want to have : "))
max_num = int(raw_input("Enter maximum number of pen you want to have : "))

print "Okay, I picked random number between " + str(min_num) + " and " + str(max_num) + ". As a result, you will have " + str(random.randint(min_num, max_num)) + " pen(s). And it will be arrived in 5 days."


# I will tell you when you are going to have this pen.
for i in range(4,0,-1):
    print "Now, your pen will be arrived in " + str(i) + " days."



