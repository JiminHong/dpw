class Main_handler:
    def __init__(self):
        print "Main created"
        utils = Utilities()
        # printing = Print()
        avg = utils.get_average([30,40,50])
        # printing.print_out(avg)
        Print().print_out(avg)



class Print:
    def __init__(self):
        # print "Print created"
        pass
    def print_out(self, r):
        print r

class Utilities:
    def __init__(self):
        # print "Utilites created"
        pass
    def get_average(self,n):
        total = 0
        for i in n:
            total += i
        average = total / len(n)
        return "Your average grade is " + str(average) +"."

main = Main_handler()