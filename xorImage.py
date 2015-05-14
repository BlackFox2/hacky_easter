from cairo._cairo import ImageSurface



__author__ = 'blackfox'
path = "/home/blackfox/Downloads/diff.png"
img = ImageSurface.create_from_png(path)
testPixel = [0,0,0,0]
originalPixel = []
#implementation to get a pixel from the image
img_width = 640
x = 498
y = 63
index = 4 * (y*img_width + x)   #four because we have 4 channels in a pixel
data = img.get_data()
originalPixel.append(ord(data[index+2]))
originalPixel.append(ord(data[index+1]))
originalPixel.append(ord(data[index]))
originalPixel.append(ord(data[index+3]))
stop = False
key = 0
while stop == False: #dummy condition
    #do the xor with the key
    for i in range(0, len(originalPixel)):
        testPixel[i] = originalPixel[i] ^ key
        """TODO convert the original pixel to hex string and xor the string with the key
        after that the resulting hex string has to be converted back to rgb values for comparison
        """
    if(testPixel[0] > 200 and testPixel[1] > 200 and testPixel[2] > 200):
        stop = True
    key += 1
    #change key

print(key)
