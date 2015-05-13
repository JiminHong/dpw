class Person(object):
    def __init__(self):
        print "person created"
        self.name = "Bob"
        self.age = 0

    def talk(self):
        print "My name is " + self.name + ", and I talk."

class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        self.id = "12345"
        print self.id + " is my id number"
    def study(self):
        print self.name + " is studying....."

s = Student()
s.study()
s.talk()
