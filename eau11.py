""" Créez un programme qui affiche la différence minimum absolue """
import sys

def is_number(string):
    """ check if string is a number"""
    if string[0] == '-':
        string = string[1:]
    return string.replace('.','',1).isdigit()

def abso(n):
    """ return absolute value of a number"""
    if n < 0:
        return -n
    return n

def string_to_int(string):
    """ convert a string to an integer """
    negativ = False
    if string[0] == '-':
        string = string[1:]
        negativ = True
    i = len(string)
    count_tens = 0
    ret = 0
    while i > 0:
        c = string[i-1]
        if is_number(c):
            n = ord(c)-48
            ret += n *(10**count_tens)
            count_tens += 1
        i-=1
    if not negativ:
        return ret
    return -ret

def abs_diff(arr):
    """ return absolute difference of an array"""
    ret_abs = float('inf')
    i = 0
    while i < len(arr):
        y = 0
        while y < len(arr):
            diff = abso(float(arr[i])-float(arr[y]))
            if diff > 0 and  diff < ret_abs:
                ret_abs = diff
            y+=1
        i+=1
    return round(ret_abs,10)

def check_array_are_number(arr):
    """ check if all elements of array are numbers"""
    for el in arr:
        if not is_number(el):
            return False
    return True


if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} list of numbers")
    sys.exit(-1)

if check_array_are_number(sys.argv[1:]):
    print(abs_diff(sys.argv[1:]))
else:
    print("Error: all arguments must be numbers")
