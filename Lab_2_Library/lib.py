class Print:
    def __init__(self):
        print "Print created"
    def print_grade(self, r):
        print "Grade : " + str(r)
    def print_total_hours(self, n):
        print "Total hours is : " + str(n)

class Utilities:
    def __init__(self):
        print "Utilites created"
    def get_working_hours(self, g):
        total = int(g) * 5 * 4
        return total