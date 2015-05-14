__author__ = 'blackfox'
import hashlib
from itertools import permutations
import os
s = "9791cbe0ae919a0330994a2d6ba26b8f0c3a1da15c73bce5fca39495881a6c90"
#s = "3f3fcbe0ae3f3f03303f4a2d6ba26b8f0c3a1da15c73bce5fca33f3f3f1a6c90" #wrong
f = open("/home/blackfox/Desktop/Hacking-Lab/HackyEaster/hashestoashes/wordlist.txt")
text = f.read()
text = text.splitlines()
#print(text)
input = ""
base = ""
basecounter = 0
wordCounter = 0
base = text[0]
counter = 0
for i in range(4, 5):
    for combo in permutations(text, i):
        #print(combo)
        input = ("".join(combo)).encode('utf-8')
        hash = hashlib.sha256(input).hexdigest()
        if counter % 500000 == 0:
            print("Still working at ", input)
        counter += 1
        if hash == s:
            print(input)
            os._exit(1)
