# This for pinging porposes 
from ast import Str
from hashlib import new
from ipaddress import ip_address
import os
from tkinter import FIRST
from tokenize import String 
#========================\
#=========================\
#==========================\
print('This Program Should Ping a range of IPs to check if they are UP or not')
FIRST_IP = input('Add Your first IP in the range: ')  #add your first IP in the range   
LAST_IP = input('Add your last IP: ')  #add your last IP in the range
#==========================/
#=========================/
#========================/
#========================\
#=========================\
#==========================\
ip_list = ['8.8.8.8'] 
#==========================/
#=========================/
#========================/
 
ask = input('Do you want to add unique IPs out of the range? (y/n): ')
if ask.casefold() == 'y':
    n = input("Enter the IPs separated by space: ") 
      
    ip_list = n.split()

editableIP = FIRST_IP

# 
#this should slice the ip into four octet and return it as a list 
def SliceIP(fullIP:str):
    octetsList = ['-1','-1','-1','-1']
    tempIP = fullIP
    n = 0
    #======================================Fourth Octet
    if fullIP[-2] == '.':
       octetsList[3] = fullIP[-1:]
    else: 
        if fullIP[-3] == '.':
            octetsList[3] = fullIP[-2:]
        else:
            if fullIP[-4] == '.':
                octetsList[3] = fullIP[-3:]
    #======================================First Octet
    while tempIP[n] != '.':
        n = n + 1
    # print(tempIP[0:n])
    octetsList[0] = tempIP[0:n] # 192.168.100.1
    tempIP = tempIP[n+1:]
    # print(tempIP)
    #======================================Second Octet
    while tempIP[n] != '.':
        n = n + 1
    # print(tempIP[0:n])
    octetsList[1] = tempIP[0:n]
    tempIP = tempIP[n+1:]
    # print(tempIP) 
    #======================================third octet
    while tempIP[n] != '.':
        n = n + 1
    # print(tempIP[0:n])
    octetsList[2] = tempIP[0:n]
    tempIP = tempIP[n+1:]
    # print(tempIP)
    
    return octetsList

#this function check if the firs ip == LAst ip and return boolean 

# check if the last octet goes up to 255, it increse the left octet and repeat from zero 
def increaseAndRepet(ip1:str):
    o1 = SliceIP(ip1)[0]
    o2 = SliceIP(ip1)[1]
    o3 = SliceIP(ip1)[2]
    o4 = SliceIP(ip1)[3]
    o1int = int(o1)
    o2int = int(o2)
    o3int = int(o3)
    o4int = int(o4)
    if o4int == 255 and o3int != 255 and o2int != 255:
        o4int = 0
        o3int = o3int + 1
        return f"{o1int}.{o2int}.{o3int}.{o4int}"
    else:
        if o4int == 255 and o3int == 255 and o2int != 255:
            o4int = 0 
            o3int = 0 
            o2int = o2int + 1 
            return f"{o1int}.{o2int}.{o3int}.{o4int}"
        else:
            if o4int == 255 and o3int ==255 and o2int == 255:
                o4int = 0
                o3int = 0 
                o2int = 0
                o1int = o1int + 1
                return f"{o1int}.{o2int}.{o3int}.{o4int}"
            else: 
                return f"{o1int}.{o2int}.{o3int}.{o4int}"
             
def nextIP(oldIP:Str):
    o1 = int(SliceIP(oldIP)[0])
    o2 = int(SliceIP(oldIP)[1])
    o3 = int(SliceIP(oldIP)[2])
    o4 = int(SliceIP(oldIP)[3])
    o4 = o4 + 1 
    newIP = f"{o1}.{o2}.{o3}.{o4}"
    newIP = increaseAndRepet(newIP)
    return newIP



while editableIP != LAST_IP:
    ip_list.append(editableIP)
    x = nextIP(editableIP)
    editableIP = x
ip_list.append(editableIP)

for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    # print(response)
    if "Received = 1" and "Approximate" in response:
        print(f"{ip} is up !")

    else:
        print (f"----------------{ip} is Down -----------------")
input("all the IPs have been checked, press enter to end..")




