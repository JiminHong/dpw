# Description

# 1. You will enter your name.
# 2. You will enter your grades of two exams.
# 3. You will enter how many hours you work daily.
# I will show you your average grade and your monthly salary.
# Same or Higher than 80 => $30/hour
# Same or Higher than 60 and lower than 79 => $20/hour
# Lower than 60 => $10/hour

from lib import *

class Main_handler:
    def __init__(self):
        # print "Main created"
        printing = Print()
        utils = Utilities()
        hours_day = raw_input("How many hours do you work a day? : ")
        grade = raw_input("Enter your grade on your final exam : ")
        name = raw_input("Enter your name : ")
        wage = utils.get_grade(grade)
        salary = utils.get_salary(hours_day, wage)
        printing.print_result(grade,hours_day,name,wage,salary)

main = Main_handler()