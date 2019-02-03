#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def conversion_dec2base(decimal,base) :
    if decimal > 0 :
        return conversion_dec2base(decimal // base, base) + [decimal % base]
    else :
        return []

def conversion(decimal) :
    dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

    hex = conversion_dec2base(decimal,16)
    hex = [dic.get(n,n) for n in hex]

    if len(hex) % 2 == 1 : # https://stackoverflow.com/a/37354069
        hex = ['0'] + hex

    big_endian = [hex[2*k:2*(k+1)] for k in range(len(hex)//2)]
    little_endian = big_endian[::-1]

    big_endian = '0x ' + ' '.join([''.join(l) for l in big_endian])
    little_endian = '0x ' + ' '.join([''.join(l) for l in little_endian])

    print("big_endian : ", big_endian)
    print("little_endian : ", little_endian)

n = 466321
conversion(n)
print("big_endian avec la fonction hex : ", hex(n))
