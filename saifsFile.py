from unittest.mock import NonCallableMagicMock
import uuid
import socket
import sys


UDP_IP = '8.8.8.8'
MAX_ATTEMPTS = 3


def sendQuery(dns_query, address, port):
    print("in send Query")

#Populates DNS query when creating it
def populateDNSQuery(dns_query):
    uuidFour = uuid.uuid4()
    dns_query["id"] = hex(int(str(uuidFour).split("-")[1], 16))
    dns_query["QR"] = hex(int("0x0", 16))
    dns_query["OPCODE"] = hex(int("0x0", 16))
    dns_query["RD"] = hex(int("0x1", 16))
    dns_query["QDCOUNT"] = hex(int("0x1", 16))
    #dns_query["QNAME"] = 
    #dns_query["QTYPE"] = 

#Host name provided by the user. 

def main():
    userInput = input("Enter Host name: ")
    print(userInput)


    if userInput == '':
        print("Please input an argument")
        exit()

    # Setting up DNS query. Only has header and question, need to prepare a message

    dns_query = {}
    populateDNSQuery(dns_query)

main()
