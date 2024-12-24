
def get_combinaisons():
    uniq = []
    uniq_set = []
    for i in range(1000):
        string = "{:03d}".format(i)
        if string[0] != string[1] and string[1] != string[2] and string[0] != string[2]:
            if set(string) not in uniq_set:
                uniq.append(string)
                uniq_set.append(set(string))
    return uniq

def pretty_print(arr):
    for s in arr[:-1]:
        print(s,end=",")
    print(arr[-1])


pretty_print(get_combinaisons())