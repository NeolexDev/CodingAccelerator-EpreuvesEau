""" Créez un programme qui affiche le premier index d’un élément recherché dans un tableau """
import sys

def index(arr,find):
    """ print first index of last element in array inside array """
    i = 0
    while i < len(arr)-1:
        if find == arr[i]:
            return i
        i+=1
    return -1

if len(sys.argv) < 3:
    print("Usage: string string string string string_to_index")
    sys.exit(-1)
print(index(sys.argv[1:],sys.argv[len(sys.argv)-1]))
