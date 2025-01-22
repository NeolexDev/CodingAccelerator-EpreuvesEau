""" programme qui implemente un tri a bulle """
import sys

def is_number(string):
    """ check if string is a number"""
    if string[0] == '-':
        string = string[1:]
    return string.replace('.','',1).isdigit()

def my_bubble_sort(array):
    """ tri a bulle """
    length = len(array)
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(1,length):
            if array[i-1] > array[i]:
                tmp = array[i-1]
                array[i-1] = array[i]
                array[i] = tmp
                not_sorted =  True
        length-=1
    return array


def check_array_are_number(arr):
    """ check if all elements of array are numbers"""
    for el in arr:
        if not is_number(el):
            return False
    return True

if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} n1 n2 ... ")
    sys.exit(-1)

if check_array_are_number(sys.argv[1:]):
    print(" ".join(my_bubble_sort(sys.argv[1:])))
else:
    print("Error: all arguments must be numbers")
    sys.exit(-1)
