""" tri par ordre ascii """
import sys


def is_max_ascii(str1,str2):
    """ return true if first argument is max in ascii """
    for i in range(min(len(str1),len(str2))):
        if ord(str1[i]) > ord(str2[i]):
            return True
        else:
            return False
    return False


def my_bubble_sort(array,max_func):
    """ tri a bulle """
    length = len(array)
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(1,length):
            if max_func(array[i-1], array[i]):
                tmp = array[i-1]
                array[i-1] = array[i]
                array[i] = tmp
                not_sorted =  True
        length-=1
    return array

def tri_ascii(array):
    """ tri ascii """
    return my_bubble_sort(array,is_max_ascii)



if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} string1 string2 ... ")
    sys.exit(-1)

print(" ".join(tri_ascii(sys.argv[1:])))
