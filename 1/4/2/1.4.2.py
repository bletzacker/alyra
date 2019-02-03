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

    big_endian_without_prefixe = ' '.join([''.join(l) for l in big_endian])
    little_endian_without_prefixe = ' '.join([''.join(l) for l in little_endian])

    big_endian = '0x ' + big_endian_without_prefixe
    little_endian = '0x ' + little_endian_without_prefixe

    length = len(''.join(little_endian_without_prefixe.split( ))) // int(2)
    if decimal <= 252 :
        variable_little_endian = little_endian
    elif decimal <= 2**16-1 :
        variable_little_endian = '0x fd ' + little_endian_without_prefixe + ' 00 ' * (2-length)
    elif decimal <= 2**32-1 :
        variable_little_endian = 'Ox fe ' + little_endian_without_prefixe + ' 00 ' * (4-length)
    else :
        variable_little_endian = 'Ox ff ' + little_endian_without_prefixe + ' 00 ' * (8-length)

    print("big_endian : ", big_endian)
    print("little_endian : ", little_endian)
    print("variable little endian : ", variable_little_endian)

n = 131
print(n)
conversion(n)
# cours : 131 -> 0x83 : OK

n = 255
print(n)
conversion(n)
# cours 255 -> 0xfdff00 : OK

n = 643
print(n)
conversion(n)
# cours 643 -> 0xfd2b83 : erreur dans le cours

n = 466321
print(n)
conversion(n)
# exercice 466321 -> 0x fe 91 1d 07 00 :
