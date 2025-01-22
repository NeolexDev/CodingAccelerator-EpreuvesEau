import sys

def n_element_fibonnaci(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    return n_element_fibonnaci(n - 1) + n_element_fibonnaci(n - 2)

if len(sys.argv) < 2:
    print("Error: need an argument",file=sys.stderr)
    sys.exit(-1)
arg1 = sys.argv[1]
if not arg1.isdigit():
    print("Error: invalid argument",file=sys.stderr)
    sys.exit(-1)
print(n_element_fibonnaci(int(arg1)))

