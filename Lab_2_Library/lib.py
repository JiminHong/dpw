class Print:
    def __init__(self):
        pass
    def print_result(self, g, h, n, w, s):
        print str(n) + ", you got " + str(g) + " on your final exam, therefore your wage per an hour is $" + str(w) + ". Since you work " + str(h) + " hour(s) a day, your monthly salary is " + str(s) + "."

class Utilities:
    def __init__(self):
        pass
    def get_wage(self, grade):
        if int(grade) >= 80:
            wage = 30
        elif int(grade) >= 60:
            wage = 20
        else:
            wage = 10
        return wage
    def get_salary(self, hours, wage):
        return int(hours) * 5 * 4 * int(wage)
