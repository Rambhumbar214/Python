import sys 
#sys used for give command line argument

if len(sys.argv) != 2:
    print("Please provide exactly one integer value as a command line argument.")
else:
    try:
        value = int(sys.argv[1])
        if 1 <= value <= 50:
            print("ok")
        else:
            print("out of range")
    except ValueError:
        print("Please provide a valid integer.")
