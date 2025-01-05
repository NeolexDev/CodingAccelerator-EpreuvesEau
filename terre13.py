""" programme qui implemente un tri par selection """
import sys

def is_number(string):
    """ check if string is a number"""
    if string[0] == '-':
        string = string[1:]
    return string.replace('.','',1).isdigit()

def my_select_sort(array):
    """ tri par selection d'un tableau """
    length = len(array)
    for i in range(length):
        min_index = i
        for c in range(i+1,length):
            if array[min_index] > array[c]:
                min_index = c
        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp
    return array


def check_array_are_number(arr):
    """ check if all elements of array are numbers"""
    for el in arr:
        if not is_number(el):
            return False
    return True

if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} n1 n2 n3 ... ")
    sys.exit(-1)

if check_array_are_number(sys.argv[1:]):
    print(" ".join(my_select_sort(sys.argv[1:])))
else:
    print("Error: all arguments must be numbers")
    sys.exit(-1)
