#!/usr/bin/python

import bluetooth

def connect ():
    bd_addr = "94:65:2D:EC:78:89"
    port = 3
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()

connect()
