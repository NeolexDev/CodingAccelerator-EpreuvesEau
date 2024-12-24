""" Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres """
import sys

def is_number(char):
    """ returns if char is a number character """
    ascii_char = ord(char)
    return (ascii_char > 47 and ascii_char < 58)


if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} \"string\" ")
    sys.exit(-1)

# Check if the first argument have at least one letter inside
ONLY_NUMBER = False
COUNT_NUMBER = 0
for c in sys.argv[1]:
    if is_number(c):
        COUNT_NUMBER+=1

ONLY_NUMBER =  len(sys.argv[1]) == COUNT_NUMBER
if ONLY_NUMBER:
    print(True)
else:
    print(False)
