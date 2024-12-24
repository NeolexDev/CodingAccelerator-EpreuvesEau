""" Créez un programme qui affiche toutes les valeurs comprises entre deux nombres"""
import sys

def is_number(char):
    """ returns if char is a number character """
    ascii_char = ord(char)
    return (ascii_char > 47 and ascii_char < 58)


def string_to_int(string):
    """ convert a string to an integer """
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
    return ret


def print_min_max(number1,number2):
    """ print all value from number1 included to number2 excluded """
    i = number1
    while i < number2:
        print(i)
        i+=1
# Check if the first argument have at least one letter inside
def check_arguments_are_number(args):
    """ check if both first arguments are string with only numbers"""
    only_number_1 = False
    count_number = 0
    for c in args[1]:
        if is_number(c):
            count_number+=1
    only_number_1 = len(args[1]) == count_number
    only_number2 = False
    count_number = 0
    for c in sys.argv[2]:
        if is_number(c):
            count_number+=1
    only_number2 = len(args[2]) == count_number
    return only_number_1 and only_number2

if len(sys.argv) != 3:
    print("Usage: python {sys.argv[0]} number number")
    sys.exit(-1)
if not check_arguments_are_number(sys.argv):
    print("Error: arguments must be numbers")
    sys.exit(-1)

n1 = string_to_int(sys.argv[1])
n2 = string_to_int(sys.argv[2])
if n1 >= n2:
    print("Error: n1 must be inforior to n2")
    sys.exit(-1)
print_min_max(n1,n2)
