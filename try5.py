import bluetooth
port = 3
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(('94:65:2D:EC:78:89', port)) 
                      #targetBluetoothMacAddress is my phone MacAddress
sock.send("hello!!")
#sock.close()
