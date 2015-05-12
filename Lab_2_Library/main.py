# Description
# 1. You will enter your name.
# 2. You will enter your grades of two exams.
# 3. You will enter how many hours you work daily.
# I will show you your average grade and your monthly salary.
# Same or Higher than 80 => $30/hour
# Same or Higher than 60 and lower than 79 => $20/hour
# Lower than 60 => $10/hour

class Main_handler:
    def __init__(self):
        # print "Main created"
        # utils = Utilities()
        printing_avg = Print()
        # avg = utils.get_average([30,40,50])
        grade = raw_input("Enter your grade on your final exam : ")
        grade = 90
        printing_avg.print_out(grade)


class Print:
    def __init__(self):
        print "Print created"
    def print_out(self, r):
        print "Grade : " + str(r)

# class Utilities:
#     def __init__(self):
#         print "Utilites created"
#     def get_average(self,n):
#         total = 0
#         for i in n:
#             total += i
#         average = total / len(n)
#         return average



main = Main_handler()