""" Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre. """
import sys


def string_dans_string(string,to_find):
    """ find if to_find is inside string """
    find_len = len(to_find)
    n = 0
    for c in string:
        if c == to_find[n]:
            n+=1
        else:
            if n > 0:
                n = 0
        if n == find_len:
            return True
    return False

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} \"string\" \"string to find\"")
    sys.exit(-1)

print(string_dans_string(sys.argv[1],sys.argv[2]))
