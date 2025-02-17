import sys

def check_range(value):
    if 1 <= value <= 50:
        print("ok")
    else:
        print("out of range")


if len(sys.argv) != 2:
    print("Please provide exactly one integer value as a command line argument.")
else:
    try:
       
        value = int(sys.argv[1])
        check_range(value)
    except ValueError:
        print("Please provide a valid integer.")
