import uuid
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

dns_query = {}

uuidFour = uuid.uuid4()
dns_query["id"] = hex(int(str(uuidFour).split("-")[1], 16))
dns_query["QR"] = hex(int("0x0", 16))
dns_query["OPCODE"] = hex(int("0x0", 16))
dns_query["RD"] = hex(int("0x1", 16))
dns_query["QDCOUNT"] = hex(int("0x1", 16))
