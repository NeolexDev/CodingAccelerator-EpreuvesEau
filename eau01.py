
def return_combinaisons():
    string = ""
    known = []
    for i in range(100):
        for y in range(100):
            if i != y and (i,y) and  set([i,y]) not in known:
                string += "{:02d} {:02d},".format(i,y)
                known.append(set([i,y]))
    return string[:-1]


print(return_combinaisons())