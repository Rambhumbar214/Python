"""WRITE A PROGRAM WHICH ACCEPTS AN INTEGER VALUE AS COMMAND LINE AND
PRINT OK IF VALUE IS BETWEEN 1 TO 50 (BOTH INCLUSIVE)
OTHERWISE IT PRINTS "OUT OF RANGE"""

import sys


if len(sys.argv) != 2:
    print("Please provide an integer value as a command-line argument.")
    sys.exit()


try:
    value = int(sys.argv[1])
   
    if 1 <= value <= 50:
        print("OK")
    else:
        print("OUT OF RANGE")
except ValueError:
    print("Please provide a valid integer.")
