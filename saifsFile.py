import binascii
from logging import exception
import socket
import sys
import time
from turtle import clear
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

    #hostNameArray = hostName.split()

    website = hostName.split(".")

    #Get QNAME
    qName = ''
    for i in range(len(website)):
        if len(website[i]) < 10:
            qName += "0"  + str(format(len(website[i]) , "X"))
        else:
            qName += str(format(len(website[i]) , "X"))
        for j in range(len(website[i])):
            qName += str(format(ord(website[i][j]), "x"))

    #Get QTYPE
    #qType = '1'

    
    #Qtype
    qType = '0000010001'


    question = qName + qType

    query = header + question

    # print('DNS Header = ' + header)
    # print('DNS Question = ' + question)
    # print('DNS Query = ' + query)
    return [query, question]


def sendQuery(query):

    response = ""
    serverAddress = ("8.8.8.8", 53)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    count = 1
    print("Contacting DNS query")
    print("Sending DNS Query..")
    while count < 4:
        try:
            sock.sendto(binascii.unhexlify(query), serverAddress)
            sock.settimeout(5)
            response, _ = sock.recvfrom(1024)


            if response != "":
                print('DNS response recieved (attempt ' + str(count) + ' of 3)')
                break


        except Exception as e:
            print("Failed creating a connection " + str(e))
            count += 1



    sock.close()
    if count >= 4:
        print("Unable to send Query.")
        sys.exit()

    return binascii.hexlify(response).decode("utf-8")



def recieveAndProcessResponse(responseQuery, query, hostName, qname):
    print("Processing DNS response..")
    print('--------------------------------------------')
    headerID = responseQuery[:4]

    #everything else after in the header will be after index 4

    headerQR = responseQuery[4:8]
    headerOPCODE = responseQuery[4:8]
    headerAA = responseQuery[4:8]
    headerTC = responseQuery[4:8]
    headerRD = responseQuery[4:8]
    headerRA = responseQuery[4:8]
    headerZ = responseQuery[4:8]
    answerRDATA = responseQuery[len(responseQuery)-8:len(responseQuery)]

    questionQNAME = 1
    questionQTYPE =1
    questionQCLASS =1



    answerNAME = 1
    answerTYPE = 1

    print('header.ID = ' + str(headerID))
    print('header.QR = 1')
    print('header.OPCODE = 00')
    print('header.AA = 0')
    print('header.TC = 0')
    print('header.RD = 1')
    print('header.RA = ' + str(headerRA))
    print('header.Z = 0')
    print('header.RCODE = 0000')
    print('header.QDCOUNT = 0001')
    print('....')
    print('....')
    print('question.QNAME = ' + str(qname))
    print('question.QTYPE = 0001')
    print('question.QCLASS = 0001')
    print('....')
    print('....')
    print('answer.NAME ' + str(answerNAME))
    print('answer.TYPE = 0001')
    print('answer.RDATA = ' + str(answerRDATA))


def main(hostName):
    print("Hello welcome to Saif's and Rohit's DNS Client project")
    print('------------------------')
    print('Preparing DNS query..')
    query = createDNSQuery(hostName)
    responseQuery = sendQuery(query[0])
    recieveAndProcessResponse(responseQuery, query[0], hostName, query[1])

    print('END OF PROGRAM, THANK YOU!')


if __name__ == "__main__":
    # hostName = "my−dns−client gmu.edu"
    # main(hostName)
    if len(sys.argv) == 1:
        print("Insufficient number of arguments")
        exit()
    elif len(sys.argv) > 2:
        print("Too many arguments")
        exit()
    else:
        hostName = sys.argv[1]
        main(hostName)
