#!/bin/python
#-*- encoding=utf8 -*-
n=input("hangi sayıya kadar olan chen asal sayısını bulalım: ")

sayi=2
kontrol=0
liste=[]
while sayi!=n -4 :
    print "work for ", sayi
    for i in range(2,sayi):
        kontrol=0
        if sayi%i==0:
            kontrol=1
            break
        else:
            kontrol=0
    if kontrol==0:
        while int(sayi+2)!=n-2:
            print "check for " , sayi
            for i in range(2,sayi+2):
                kontrol=0
                if (sayi+2)%i==0:
                    kontrol=1
                    break
                else:
                    kontrol=0
            if kontrol==0:
                 liste.append(sayi)
    	    sayi=sayi+1
print liste
