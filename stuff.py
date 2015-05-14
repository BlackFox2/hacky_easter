__author__ = 'blackfox'
"""
from itertools import product
import hashlib
print(hashlib.algorithms_available)
h = hashlib.new("SHA224")
h.update("test".encode('utf-8'))
print(h.hexdigest())
h = hashlib.sha224("test".encode('utf-8')).hexdigest()
print(h)
s = "test"
"""
"""
import base64
import binascii
s = "a791KNndKVmnr7N4mEJfZ1VfZ/Z3mHyufoYhCiyKDb38JI7C17JAEPRAutwiI7S1"
res = base64.b64decode(s)
res = binascii.hexlify(res)
print(res)
"""
"""
from itertools import permutations
i = open("/home/blackfox/Desktop/Hacking-Lab/HackyEaster/hashestoashes/wordlist.txt")
o = open("/home/blackfox/Desktop/Hacking-Lab/HackyEaster/hashestoashes/fourword.txt", 'w')
strings = i.read()
strings = strings.splitlines()
for i in range(0,5):
    for combo in permutations(strings, i):
        input = "".join(combo)
        o.write(input)
        o.write('\n')
"""
from Crypto.Hash import MD5
m = MD5.new()
m.update('aaaaab'.encode('utf-8'))
print(m.hexdigest())
