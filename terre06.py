""" Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. """
import sys

def is_letter(char):
    """ returns if char is a letter """
    ascii_c = ord(char)
    return (ascii_c > 96 and ascii_c < 123) or (ascii_c > 64 and ascii_c < 91)

def is_minuscule(char):
    """ returns is char is a minuscule letter """
    ascii_c = ord(char)
    return ascii_c > 96 and ascii_c < 123

def alternate_maj(string):
    """ fix one maj on two letters """
    ret_str = ""
    i = 0
    for char in string:
        if is_letter(char):
            if i%2 == 0 and is_minuscule(char):
                ret_str += chr(ord(char)-32)
            else:
                ret_str += char
            i+=1
        else:
            ret_str += char
    return ret_str


if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} \"string\" ")
    sys.exit(-1)

GOT_LETTER = False
for c in sys.argv[1]:
    if is_letter(c):
        GOT_LETTER = True
        break

if GOT_LETTER:
    print(alternate_maj(sys.argv[1]))
else:
    print("Error: first argument must have at least one letter")
    sys.exit(-1)
