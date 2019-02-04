#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Utilisation de l'API de https://blockchain.info/
# pip install blockchain
from blockchain import blockexplorer

import time
now = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())

height_latest_block = blockexplorer.get_latest_block().height
print("Nous pouvons calculer précisément la taille de l’ensemble des en-têtes.")
print("Nous multiplions la taille d'une en-tête (80 octets) par le nombre de blocs à ce jour : ",height_latest_block)
print("Taille de l’ensemble des en-têtes le ", now, ": ", 80 * height_latest_block / 1e6, "Mo")
# 2019-02-04 06:30:05 UTC :  44.91696 Mo
