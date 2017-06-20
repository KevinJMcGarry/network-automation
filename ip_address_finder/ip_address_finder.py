# Function for carving ip addresses out of a file.

import re

def IPAddressCarver(input):
    return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

def getIPAddresses(fileName):
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            found_ips = IPAddressCarver(line)
            ipAddressList.append(found_ips)

ipAddressList = []

fileName = input('Enter the name of the file/path you wish to search for IP Addresses: ')

getIPAddresses(fileName)

print(ipAddressList)
