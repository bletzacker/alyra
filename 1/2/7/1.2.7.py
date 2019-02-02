#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

def fonction_hash(key) :
    n = 8
    hash = hashlib.sha1(str.encode(key))
    return int(hash.hexdigest(), 16) % n

def ajouter(table_hachage,data) :
    (key,value) = data
    i = fonction_hash(key)
    table_hachage[i].append(data)
    return table_hachage

def rechercher(table_hachage,found_key) :
    i = fonction_hash(found_key)
    return [(key,value) for (key,value) in table_hachage[i] if key == found_key]


table_hachage = [[],[],[],[],[],[],[],[]]
# https://stackoverflow.com/a/33513257

ajouter(table_hachage,("153.8.223.72","Amsterdam"))
ajouter(table_hachage,("169.38.84.49","Chennai"))
ajouter(table_hachage,("169.46.49.112","Dallas"))
ajouter(table_hachage,("184.173.213.155","Dallas, TX, USA"))
ajouter(table_hachage,("159.122.100.41","Frankfurt"))
ajouter(table_hachage,("119.81.134.212","Hong Kong"))
ajouter(table_hachage,("5.10.5.200","London"))
ajouter(table_hachage,("158.176.81.249","London"))
ajouter(table_hachage,("168.1.168.251","Melbourne"))
ajouter(table_hachage,("169.57.7.230","Mexico City"))
ajouter(table_hachage,("159.122.142.111","Milan"))
ajouter(table_hachage,("159.8.78.42","Paris"))
ajouter(table_hachage,("192.155.217.197","San Jose"))
ajouter(table_hachage,("169.57.163.228","São Paulo"))
ajouter(table_hachage,("169.56.184.72","Toronto"))
ajouter(table_hachage,("50.87.60.166","Washington DC"))

print(table_hachage)
print(rechercher(table_hachage,"159.8.78.42"))
print(rechercher(table_hachage,"159.122.142.111"))
