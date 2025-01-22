import sys

def is_integer(s):
    """ Returns True if string is a number. """
    return s.isdigit()



def is_prime(n):
    ''' check if n is prime number '''
    if n < 2 or (n>2 and n%2==0):
        return False
    for i in range(3,n):
        if n%i == 0:
            return False
    return True

def find_next_prime(n):
    """ find next prime number """
    i = n+1
    while True:
        if is_prime(i):
            return i
        i+=1


if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} number")
    sys.exit(-1)
if not is_integer(sys.argv[1]):
    print("Error: First argument expected to be a positive integer")
    sys.exit(-1)
print(find_next_prime(int(sys.argv[1])))
