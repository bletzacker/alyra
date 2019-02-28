#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install console-menu
from consolemenu import *
from consolemenu.items import *

from converter import *

def cm_hexadecimal2decimal():
    Screen().println(str(hexadecimal2decimal(Screen().input('Enter a hexadecimal without Ox : ').input_string)))
    Screen().input('Press [Enter] to continue')

def cm_decimal2hexadecimal():
    Screen().println(decimal2hexadecimal(int(Screen().input('Enter a decimal : ').input_string)))
    Screen().input('Press [Enter] to continue')

def cm_hexadecimal_little_endian2decimal():
    Screen().println(str(hexadecimal_little_endian2decimal(Screen().input('Enter a hexadecimal little-endian without 0x : ').input_string)))
    Screen().input('Press [Enter] to continue')

def cm_varInt2decimal():
    Screen().println(str(varInt2decimal(Screen().input('Enter a varInt without 0x : ').input_string)))
    Screen().input('Press [Enter] to continue')

def cm_bits2target():
    Screen().println(str(bits2target(Screen().input('Enter a bits without 0x : ').input_string)))
    Screen().input('Press [Enter] to continue')

def cm_target2difficulty():
    Screen().println(str(target2difficulty(int(Screen().input('Enter a target in decimal : ').input_string))))
    Screen().input('Press [Enter] to continue')

def cm_decode_transaction():
    decode_transaction(Screen().input('Enter a raw bitcoin hexadecimal transaction : ').input_string)
    Screen().input('Press [Enter] to continue')

def cm_decode_block():
    decode_block(Screen().input('Enter a block hash : ').input_string)
    Screen().input('Press [Enter] to continue')

def cm_navigate():
    Screen().println(str(navigate(Screen().input('Enter a hexadecimal : ').input_string)))
    Screen().input('Press [Enter] to continue')

def menu() :
    menu = ConsoleMenu("Challenge 1", "Bitcoin analysis tool")
    submenu1 = ConsoleMenu("Converter")
    submenu1_item = SubmenuItem("Converter", submenu1, menu)
    submenu1.append_item(FunctionItem("Hexadécimal -> décimal", cm_hexadecimal2decimal))
    submenu1.append_item(FunctionItem("Décimal -> hexadécimal", cm_decimal2hexadecimal))
    submenu1.append_item(FunctionItem("Hexadécimal little endian -> hexadécimal", cm_hexadecimal_little_endian2decimal))
    submenu1.append_item(FunctionItem("varInt -> décimal", cm_varInt2decimal))
    submenu1.append_item(FunctionItem("Champ Bits -> Cible correspondante", cm_bits2target))
    submenu1.append_item(FunctionItem("Cible -> Difficulté", cm_target2difficulty))
    submenu2 = ConsoleMenu("Decode Raw Bitcoin Hexadecimal Transaction or Block")
    submenu2_item = SubmenuItem("Decode Raw Bitcoin Hexadecimal Transaction or Block", submenu2, menu)
    submenu2.append_item(FunctionItem("Decode Raw Bitcoin Hexadecimal Transaction", cm_decode_transaction))
    submenu2.append_item(FunctionItem("Decode Raw Bitcoin Hexadecimal Block", cm_decode_block))
    submenu3 = ConsoleMenu("Navigate the bitcoin blockchain")
    submenu3_item = SubmenuItem("Navigate the bitcoin blockchain", submenu3, menu)
    submenu3.append_item(FunctionItem("Navigate the bitcoin blockchain", cm_navigate))
    menu.append_item(submenu1_item)
    menu.append_item(submenu2_item)
    #menu.append_item(submenu3_item)
    menu.show()
