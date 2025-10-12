x ='sinan'
type(x)
x.capitalize()

def topla(deger, deger2):
    print("{}, {} degerlerini alır".format(deger, deger2))

def selam():
    print("selam")

topla(3, 5)
selam()

help(print)
selam()

def selamGotur(isim):
    print("selam", isim)

selamGotur("sinan")

def topla():
    print("toplama yapan fonks.")

def topla(a, b):
    c = a + b
    return c

topla(3, 5)

def kareal(a):
    return a * a

sonuc = kareal(4)
print("istenilen değerin karesi {}: ".format(sonuc))
sonuc = kareal(8)
print("istenilen değerin karesi ", sonuc)

print("sinan")

def selam(d):
    print("grilen deger", d)

help(format)  # ?format
a = int(input("1. sayıyı giriniz: "))
b = int(input("2. sayıyı giriniz: "))

def cikar(x, y):
    print("sonuc :", a - b)

    return a - b

def kareal(x):
    # print("a nın karesi:",a*a)

    return a * a

sonuc = cikar(a, b)
kareal(a)
cikar(5, 5)

def ceyrek(x):
    return x / 4

def küpal(x):
    return x * x * x

küpal(3)
ceyrek(4)
küpal(ceyrek(12))
print(küpal(ceyrek(20)))
liste1 = [1, 2, 3, 4, 5]
liste1
liste2 = [i * 2 for i in liste1]
liste2
kare = lambda x: x * x  # kare al fonksiyonu yerine

def toplama(x, y):
    return x + y

toplama(5, 5)
# lambda ile
toplama = lambda x, y: x + y
toplama(5, 5)

import math as matematik

matematik.pow(2, 2)

matematik.cos(60)
matematik.sin(60)
matematik.sqrt(4)
from math import *
import time
import random

rastgele = random.randint(1, 100)

import random
import time

rastgele = random.randint(1, 100)
tahmin = 5

while True:

    tahmin = int(input("tahmin gir 1-100 arası :"))
    print("kontrol ediliyor")

    if tahmin == rastgele:
        print("kontrol ediliyor")

        time.sleep(1)

        print("girilen sayi", tahmin)
        break

        print("tebrikler")
    elif tahmin < rastgele:
        tahmin = tahmin - 1
        print("sayıyı büyült")
    elif tahmin > rastgele:
        tahmin = tahmin - 1
        print("sayıyı küçült")

    else:
        print("1-100 de değer gir")

    if tahmin == 0:
        print("hak bitti")
        break