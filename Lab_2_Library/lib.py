class Print:
    def __init__(self):
        print "Print created"
    def print_grade(self, r):
        print "Grade : " + str(r)
    def print_total_hours(self, h):
        print "Total hours is : " + str(h)
    def print_name(self, n):
        print "Your name is : " + n

class Utilities:
    def __init__(self):
        print "Utilites created"
    def get_grade(self, grade):
        if int(grade) >= 80:
            wage = 30
        elif int(grade) >= 60:
            wage = 20
        else:
            wage = 10
        # print "grade is : " + str(grade) + ". And wage is " + str(wage)
    def get_working_hours(self, g):
        total = int(g) * 5 * 4
        return total