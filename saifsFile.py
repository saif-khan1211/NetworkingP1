import binascii
from logging import exception
import socket
import sys
import time
from xmlrpc import server

def createDNSQuery(hostName):
    dnsQuery = {}

    #prepare the header

    #Revelevent Fields
    dnsQuery['ID'] = 'AAAA'
    dnsQuery['queryParams'] = '0100'
    dnsQuery['RD'] = '0001'
    #dnsQuery['QDCOUNT'] = '0000000000000001'
    dnsQuery['QDCOUNT'] = '000000000000'


    header = dnsQuery['ID'] + dnsQuery['queryParams'] + dnsQuery['RD'] + dnsQuery['QDCOUNT']

    #prepare the question

    question = ""

    hostNameArray = hostName.split()
    
    website = hostNameArray[1].split('.')

    #Get QNAME
    qName = ''
    for i in range(len(website)):
        qName += str(len(website[i]))
        print(qName)
        for j in range(len(website[i])):
            qName += str(format(ord(website[i][j]), "x"))
    
    #Get QTYPE
    #qType = '1'
    qType = '0000010001'


    #question = qName + qType
    question = qName

    query = header + question

    print('DNS Header = ' + header)
    print('DNS Question = ' + question)
    print('DNS Query = ' + query) 


def sendQuery(query):
    query = 'AAAA01000001000000000000036564750000010001'

    print(query)
    response = ""
    serverAddress = ("8.8.8.8", 53)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    count = 1
    print("Going into Loop!!!!")
    while count < 4: 
        print("IN THE LOOOOOP")
        try:
            print('Attempt - ' + str(count))
            sock.sendto(binascii.unhexlify(query), serverAddress)
            sock.settimeout(5)
            response, _ = sock.recvfrom(1024)

            if response != "":
                print("Successfull")
                break

        
        except Exception as e:
            print("Failed creating a connection " + str(e))
            count += 1



    sock.close()  
    if count >= 4:
        print("Unable to send Query.")
        sys.exit()
    
    print('Query response retreived')
    return binascii.hexlify(response).decode("utf-8")

    

def recieveAndProcessResponse(responseQuery):
    print("In recieve and ResponseQuery")

def main(hostName):

    #print('-----HELLO, WELCOME TO DNS CLIENT-----')
    #print('-------Please Enter a Host Name-------')
    query = createDNSQuery(hostName)
    #print('--------------------------------------')
    #print('-------------Sending Query------------')
    responseQuery = sendQuery(query)
   # print('------------Recieving Query-----------')
    #recievedQuery = recieveAndProcessResponse(responseQuery)

    # print('END OF PROGRAM, THANK YOU!')


if __name__ == "__main__":
    #hostName = sys.argv[1]
    #  my−dns−client gmu.edu
    #hostName = input('Enter hostName ')
    hostName = "my−dns−client gmu.edu"
    main(hostName)
