__author__ = 'blackfox'
import qrtools
import os
qr = qrtools.QR()
f = open("/home/blackfox/Desktop/leet_tv_output.txt", "w")
for file in sorted(os.listdir("/home/blackfox/Desktop/QRS")):
    if file.endswith(".png"):
        #print(file)
        qr.decode("/home/blackfox/Desktop/QRS/"+file)
        f.write(qr.data+'\n')
        print(qr.data)