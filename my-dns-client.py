import socket
import sys

if len(sys.argv) == 1:
    print("Insufficient number of arguments")
    exit()
elif len(sys.argv) > 2:
    print("Too many arguments")
    exit()
else:
    hostname = sys.argv[1]



