__author__ = 'blackfox'
import re
from copy import deepcopy
import sys
from binascii import unhexlify

def analyseXors(xored, text, index):
    string = deepcopy(text)
    helper = string[index];
    for x in range(index+1,len(string)):
        string[x-1] = string[x]
    #string[index] = string[len(string)-1]
    string[len(string)-1] = helper
    noChance = False
    for x in range(0, len(xored)):
        for i in range(0, len(xored[x])):
            if chr(xored[x][i]) == '\0':
                # both same characters
                if string[len(string)-1][i] != " " and not 'a' <= string[len(string)-1][i] <= 'z':
                    string[len(string)-1][i] = "."
                    string[x][i] = "."
                else:
                    if 'a' <= string[len(string)-1][i] <= 'z':
                        string[x][i] = string[len(string)-1][i]
                    else:
                        string[x][i] = " "
            elif 'A' <= chr(xored[x][i]) <= 'Z':
                # one of them is a space and one a lowercase letter
                #check if there also a capital letter in the next xored string at the same position => the space is in the last string
                if string[len(string)-1][i] == " ":
                    isSpaceInLast = True
                else:
                    if x + 1 < len(xored)-1:
                        for counter in range(x + 1, len(xored)):
                            if 'A' <= chr(xored[counter][i]) <= 'Z':
                                #the last one is the space (at least it seems so. it's still possible that the strings we
                                # analyze have spaces in the exact same place
                                isSpaceInLast = True
                            elif chr(xored[counter][i]) == ' ':
                                #think about
                                x = 5
                            elif chr(xored[counter][i]) == "\0":
                                #both are the same character (the actual and the last one have spaces)
                                isSpaceInLast = True
                            #and (int(string[len(string) - 1][i], 16) ^ int(string[len(string) - 1][i], 16)) != 0:

                            else:
                                isSpaceInLast = False
                                break
                    else:
                        if 'a' <= string[len(string)-1][i] <= 'z':
                            isSpaceInLast = False
                        else:
                            for counter in range(x-1, 0, -1):
                                if i > len(xored[counter])-1:
                                    #old strings are shorter then we are working at
                                    #there' no possiblity anymore to determine the spaces/letters. only if they are the same
                                    noChance = True
                                    break
                                if 'A' <= chr(xored[counter][i]) <= 'Z':
                                    #the last one is the space (at least it seems so. it's still possible that the strings we
                                    # analyze have spaces in the exact same place
                                    isSpaceInLast = True
                                elif chr(xored[counter][i]) == ' ':
                                    #think about
                                    x = 5
                                elif chr(xored[counter][i]) == "\0":
                                    #both are the same character (the actual and the last one have spaces)
                                    isSpaceInLast = True
                                #and (int(string[len(string) - 1][i], 16) ^ int(string[len(string) - 1][i], 16)) != 0:

                                else:
                                    isSpaceInLast = False
                                    break
                if noChance == True:
                    continue
                if isSpaceInLast == True:
                    #save the space at position for the last string
                    if string[len(string)-1][i] == ".":
                        #we just solved something which wasn't possible before because there were more spaces in more than the last string
                        for y in range(0,x):
                            if chr(xored[y][i]) == '\0':
                                string[y][i] = " "
                            else:
                                string[y][i] = chr(xored[y][i]).lower()
                    elif string[len(string)-1][i] == '#':
                        for y in range(0,x):
                            string[y][i] = chr(xored[y][i]).lower()
                    string[len(string)-1][i] = " "
                    string[x][i] = chr(xored[x][i]).lower()
                else:
                    #save the space at position for the actual compared string
                    if string[len(string)-1][i] == ".":
                        string[len(string)-1][i] = chr(xored[x][i]).lower()
                        for y in range(0,x):
                            if xored[y][i] == 0:
                                string[y][i] = chr(xored[x][i]).lower()
                            elif string[y][i] == '#':
                                string[y][i] = chr(xored[y][i] ^ ord(string[len(string)-1][i])).lower()
                    elif string[len(string)-1][i] == "#":
                        string[len(string)-1][i] = chr(xored[x][i]).lower()
                        for y in range(0,x):
                            if string[y][i] == '#':
                                string[y][i] = chr(xored[y][i] ^ ord(string[len(string)-1][i])).lower()

                        string[len(string)-1][i] = chr(xored[x][i]).lower()
                    string[x][i] = " "
                    string[len(string)-1][i] = chr(xored[x][i]).lower()
            else:
                string[x][i] = "#"
                if len(string[len(string)-1][i]) > 1 or string[len(string)-1][i] == '#':
                    string[len(string)-1][i] = '#'
                elif 'a' <= string[len(string)-1][i] <= 'z':
                    string[x][i] = chr(xored[x][i] ^ ord(string[len(string)-1][i])).lower()

            """if x - 1 >= 0 and not i > len(xored[x - 1]) - 1:
                if 'A' <= chr(xored[x - 1][i]) <= 'Z':
                    string[len(ciphers) - 1][i] = " "
                    string[x][i] = chr(xored[x][i]).lower()
                else:
                    #save the space at position for the actual compared string
                    string[x][i] = " "
                    string[len(ciphers) - 1][i] = chr(xored[x][i]).lower()"""
    helper = string[len(string)-1]
    for x in range(len(string)-1,index,-1):
        string[x] = string[x-1]
    string[index] = helper
    return string

def doXor(index):
    xored = []
    temp = []
    for x in range(0, len(text)):
        if x == index:
            continue
        for i in range(0, len(text[index])):
            if not i > len(text[x]) - 1:
                temp.append(int(text[index][i], 16) ^ int(text[x][i], 16))
            else:
                continue
        xored.append(temp)
        temp = []
    return xored

fin = open("/home/blackfox/Desktop/ciphers.txt", "r");
ciphers = (fin.read()).split('\n')
ciphers.sort(key=lambda s: len(s))
print(ciphers)
regex = re.compile(r"[abcdefghijklmnopqrstuvwxyz\s]*")

text = []
temp = ciphers[0]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])
temp = ciphers[1]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])
temp = ciphers[2]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])
temp = ciphers[3]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])
temp = ciphers[4]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])
temp = ciphers[5]
text.append([temp[i:i + 2] for i in range(0, len(temp), 2)])

#xored = doXor(len(text)-1)
#result = analyseXors(xored, text)
result = []
buffer = list()


for i in range(0,len(text)):
    xored = doXor(i)
    buffer = analyseXors(xored, text, i)    #testweise 5, nach umstellung muss selbes ergebnis wie vorher ruaskommen
    result.append(buffer)
    buffer = []

print(result)



for x in result:
    for i in range(0,len(x)):
        for y in range(0, len(x[i])):
            if 'a' <= x[i][y] <= 'x' or x[i][y] == ' ' or x[i][y] == '.' or x[i][y] == '#':
                if not 'a' <= text[i][y] <= 'z' or text[i][y] == '.':
                    text[i][y] = x[i][y]

for i in text:
    for x in i:
        print(x, end="")
    print("")
