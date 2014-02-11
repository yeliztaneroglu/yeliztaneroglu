# -*- coding: utf-8 -*-
sayi=input("bir sayı giriniz: ")
sayac=0
for i in range(1,sayi+1):
    if sayi%i==0:
        sayac=sayac+1
if sayi%sayac==0:
    print sayi,"tau sayısıdır."
else:
    print sayi,"tau sayısı değildir."
