import sys

def print_reverse(arr):
    for i in range(len(arr),0,-1):
        print(arr[i-1])

if len(sys.argv) < 2:
    print("error",file=sys.stderr)
    sys.exit(-1)

print_reverse(sys.argv[1:])