import os

__author__ = 'blackfox'
import base64
import binascii
import hashlib
from itertools import product
import threading
from threading import Thread
from itertools import permutations
#s = "ca73f494c11ad85db7f9cdaa657da8f237ea7dee14463e319bf8d4b3" #1700117901910710
s = "72614c75362b65416d46656c66322f7553792f36376954713537453d" #original hash
s2 = "4b89da062dd9c640e0834195ba35101fff2fe0dcca2b80a6dff9786f"
# print(binascii.hexlify(b'\xb8\x08\x14\xc5\xe0\xf3\x86\xb0cqc\xfd\x8a\xfe\xa9)'))
# print(len("6c35484c344b36526d674d776d556f7461364a726a7777364861466363377a6c2f4b4f556c596761624a413d"))
#print(binascii.a2b_hqx(s))
m = hashlib.new("SHA224")
output = ""
digits = '0179'
num_threads = 16

class ProducerThread(Thread):

    def __init__(self):
        self.threads = []
    def produce(self):
        print()
        inputcounter = 0
        threadcounter = 0
        for combo in product(digits, repeat=2):
            if threadcounter < num_threads:
                start = "".join(combo[0:2])
                print(start)
                self.threads.append(ConsumerThread(start, 14))
                threadcounter += 1


class ConsumerThread(Thread):
    def __init__(self, start, digit_count):
        self.start = start
        self.digit_count = digit_count
        self.thread = Thread(target=self.hasher, args=())
        self.thread.start()
        self.m = hashlib.new("SHA224")

    def hasher(self):
        m = hashlib.new('SHA224')
        hash_counter = 0
        for combo in product(digits, repeat=self.digit_count):
            input = self.start
            input += "".join(combo)
            #print(input)
            hash_counter += 1
            hash = hashlib.sha224(input.encode('utf-8')).hexdigest()
            m.update(input.encode('utf-8'))
            hash2 = m.hexdigest()
            if hash_counter % 300000 == 0:
                print(hash_counter, end="")
                print('-', end="")
                print(threading.current_thread().name, end="")
                print('-', end="")
                print(input)
            if hash == s or hash2 == s:
                print(input)
                os._exit(1)
                break

counter = 0
producer = ProducerThread()
producer.produce()
"""
for combo in permutations(digits, 4):
    if counter % 3 == 0:
        string = (''.join(combo)).encode('utf-8')
        print("start")
        print(string.decode('ascii'))
        t = Thread(target=hasher, args=(string.decode('ascii'),))
        t.start()
    counter += 1
"""
"""
for combo in product(digits, repeat=16):
    input = (''.join(combo)).encode('utf-8')
    hash = hashlib.sha224(input).hexdigest()
    print(input)
    if hash == s2:
        print(combo)
        break
"""
"""
613739314b4e6e644b566d6e72374e346d454a665a3156665a2f5a336d487975666f59684369794b446233384a49374331374a41455052417574776949375331

SHA224("") =
d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f
SHA256("") =
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
SHA384("") =
38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b
SHA512("") =
cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e


6c35484c344b36526d674d776d556f7461364a726a7777364861466363377a6c2f4b4f556c596761624a413d
"""

#72614c75362b65416d46656c66322f7553792f36376954713537453d