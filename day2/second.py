import random

class Helicopter:
    #construction function
    def __init__(self):
        print "Helicopter created!"
        self.model = ""
        self.speed = 0
    def fly(self):
        pass
    def take_off(self):
        print "Taking off"
    def fire_missile(self):
        print "Missile fired"

helicopter1 = Helicopter()

fleet = []

for i in range(0,10):
    helicopter = Helicopter()
    # have random number of speed
    helicopter.speed = random.randint(2, 100)
    fleet.append(helicopter)

def get_speed():
    count = 1
    for helicopters in fleet:
        print str(count) + "th helicopter has speed of " + str(helicopters.speed)
        count += 1
# Calling the function
get_speed()