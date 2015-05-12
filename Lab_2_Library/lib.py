class Print:
    def __init__(self):
        print "Print created"
    # def print_grade(self, g):
    #     print "Grade : " + str(g)
    # def print_total_hours(self, h):
    #     print "Total hours is : " + str(h)
    # def print_name(self, n):
    #     print "Your name is : " + n
    def print_result(self, g, h, n, w, s):
        print str(n) + ", you got " + str(g) + " on your final exam, therefore your wage per an hour is $" + str(w) + ". Since you work " + str(h) + " hour(s) a day, your monthly salary is " + str(s) + "."

class Utilities:
    def __init__(self):
        print "Utilites created"
    def get_wage(self, grade):
        if int(grade) >= 80:
            wage = 30
        elif int(grade) >= 60:
            wage = 20
        else:
            wage = 10
        return wage
    def get_salary(self, hours, wage):
        total = int(hours) * 5 * 4 * int(wage)
        return total