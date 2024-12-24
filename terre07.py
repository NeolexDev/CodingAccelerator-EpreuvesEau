""" Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères """
import sys

def is_letter(char):
    """ returns if char is a letter """
    ascii_c = ord(char)
    # Check if its a lowercase or uppercase letter
    return (ascii_c > 96 and ascii_c < 123) or (ascii_c > 64 and ascii_c < 91)


def is_lowercase(char):
    """ returns is char is a lowercase letter """
    ascii_c = ord(char)
    # Check if ascii is in range of lowercase asciis
    return ascii_c > 96 and ascii_c < 123

def is_space(char):
    """ returns is char is a space character """
    ascii_c = ord(char)
    # Check for character space \t \r \n
    return ascii_c == 32 or ascii_c == 0 or ascii_c == 10 or ascii_c == 13

def capitalize(string):
    """ fix one maj on two letters """
    ret_str = ""
    last_is_space = True
    for char in string:
        if is_space(char):
            last_is_space = True
            ret_str+=char
        else:
            if last_is_space:
                if is_lowercase(char):
                    # append the char in majuscule
                    ret_str += chr(ord(char)-32)
                else:
                    ret_str += char
            else:
                ret_str += char
            last_is_space = False
    return ret_str



if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} \"string\" ")
    sys.exit(-1)

# Check if the first argument have at least one letter inside
GOT_LETTER = False
for c in sys.argv[1]:
    if is_letter(c):
        GOT_LETTER = True
        break

if GOT_LETTER:
    print(capitalize(sys.argv[1]))
else:
    print("Error: first argument must have at least one letter")
    sys.exit(-1)