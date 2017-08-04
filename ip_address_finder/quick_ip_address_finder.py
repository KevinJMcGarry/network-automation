'''
quick script (not using functions) to create a sorted list of ip addresses used in a file
''' 

ipAddressList = []
ipAddressDict = {}
ipAddressList2 = []


import os, re
os.chdir('../../Downloads')
print(os.getcwd())
with open('./pathToFile', 'r') as inputfile:
    for line in inputfile:
        foundIPs = re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', line)
        ipAddressList.extend(foundIPs)

print(ipAddressList)


for element in ipAddressList:
    if element not in ipAddressDict:
        ipAddressDict[element] = 1
    else:
        ipAddressDict[element] = ipAddressDict[element] + 1

print(ipAddressDict)
for k,v in ipAddressDict.items():
    ipAddressList2.append((v,k))
print(ipAddressList2.sort())