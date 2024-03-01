#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet REIN")
os.system("figlet VPN KONTROL ARACI")

print("""
      
VPN Kontrol Aracına Hoşgeldin...
      
      """)

hedefip=input("Hedef ip : ")
os.system("ike-scan "+hedefip)