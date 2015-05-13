class Bird(object):
    def __init__(self):
        print "bird created"
        self.name = ""
        self.feather_type = "cool looking"
    def fly(self):
        print "My name is " + self.name + "!!!"
        print "I flapped and I fly toward the sky"


class Duck(Bird):
    def __init__(self):
        print "Duck created"
        super(Duck, self).__init__()
        self.quack = "QUACK"
    def fly(self):
        print "I can fly blindfolded!! XD"
        super(Duck, self).fly()

# instantiate birds!!!
d = Duck()
d.name = "Ducggie"
d.fly()