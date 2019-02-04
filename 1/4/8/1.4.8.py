#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import ctypes

max_size_unsigned = 2**(4*8)-1
print("Le timestamp du protocole Bitcoin est encodé sur 4 octets et plus précisément en uint32_t, un entier 32 bits non signé.\n ")
print("La taille maximale du timestamp est donc 2^32-1 soit : ",max_size_unsigned,"s\n" )
print("Le bug aura donc lieu le : ", time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(max_size_unsigned)), " soit en l'an ", time.strftime('%Y', time.gmtime(max_size_unsigned)))
print("La seconde d'après, la date serait : ", time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(ctypes.c_uint32(max_size_unsigned+1).value)))
