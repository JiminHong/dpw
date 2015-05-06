
def get_average(g):
    total = 0
    for grade in g:
        total += grade
    avg = total/len(g)
    return avg

print get_average([10,20,30])

name = "scott"
for letter in name:
    print letter
