__author__ = 'blackfox'
import hashlib
from Crypto.Hash import MD2
from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from itertools import product
import os
target_hash = "757c479895d6845b2b0530cd9a2b11" #original hash

#target_hash = "4ae2e4cc3750845b2b0530cd9a2b11" # test hash (aaaaaaaaaaab......
algorithms = ['md2', 'md5', 'sha1', 'sha256', 'sha512']
bitwidth = 6

input = []
hash_function = []
hash_function.append(MD2.new())
hash_function.append(MD5.new())
hash_function.append(SHA.new())
hash_function.append(SHA256.new())
hash_function.append(SHA512.new())

temp_res = []
temp_res.append("")
temp_res.append("")
temp_res.append("")
temp_res.append("")
temp_res.append("")

temp_input = []
temp_input.append("")
temp_input.append("")
temp_input.append("")
temp_input.append("")
temp_input.append("")
result = ""
i = 1
chars = "abcdefghijklmnopqrstuvwxyz1234567890!"
allPartsFound = False
counter = 0
for combo in product(chars, repeat=6):
    input = "".join(combo).encode('utf-8')
    hash_function[0] = MD2.new()
    hash_function[1] = MD5.new()
    hash_function[2] = SHA.new()
    hash_function[3] = SHA256.new()
    hash_function[4] = SHA512.new()
    allPartsFound = True
    for i in range(0,len(hash_function)):
        if not temp_res[i][i*6:i*6+6] == target_hash[i*6:i*6+6]:
            allPartsFound = False
            hash_function[i].update(input)
            temp_res[i] = hash_function[i].hexdigest()
            temp_input[i] = input
    if allPartsFound == True:
        for x in temp_input:
            print("RESULT:")
            print(x, end="")
            print(temp_input)
            os._exit(1)
    counter += 1
    if counter % 1000000 == 0:
        print(temp_input)
