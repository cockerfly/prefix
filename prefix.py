#!/usr/bin/env python
from bitcoin import *
import multiprocessing
from bit import Key
print('----------VanitySearch for public----------')
a = int(input("Generate from(number in decimial: "))
b = int(input("Generate to(number in decimial: "))
v = str(input("Input prefix of public: "))
count = 0
c = v[2:]
d = len(v)
    #z = random.randrange(1, 5)
while a < b:
    key = Key.from_int(a)
    w = key.public_point
    l = key.to_wif()
    pubKeyCompressed = '0' + str(2 + w.y % 2) + str(hex(w.x)[2:])
    coun1 = len(pubKeyCompressed)
    if coun1 == 65:
        pubKeyCompressed = '0' + str(2 + w.y % 2) + '0' + str(hex(w.x)[2:])    
        #v = '047ed0b3' 
    publ = pubKeyCompressed[2:d]
    if c in publ:
        g=open(u"pref.txt","a")
        g.write(l + '\n' + pubKeyCompressed + '\n' + str(count) + '\n')
        g.close
    a += 1
    count +=1
    print('privat:', l)
    print('public_pref:', publ) 
    print(count)

     







