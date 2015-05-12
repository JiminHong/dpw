crazy = ["scott",[3,[5,6,7]],["c","d","e"]]

# for i in range(len(crazy)):
#     for e in crazy[i]:
#         print e

# for outer in crazy:
#     for inner in outer:
#         print inner

total = 0
for outer in crazy:
    for inner in outer:
        print inner
        total +=1
print "total is " + str(total)