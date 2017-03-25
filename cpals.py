# CryptoPals Challenges www.cryptopals.com

import codecs
import binascii
import sys
import re

def bxor(b1, b2): # use xor for bytes as string! WOOT
    if type(b1) is str:
        b1 = codecs.decode(b1,"hex")
    if type(b2) is str: 
        b2 = codecs.decode(b2,"hex")
    result = b""
    for b1, b2 in zip(b1, b2):
        result += bytes([b1 ^ b2])
    return result

"""
print("Challenge 1\n")
hexstring1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print("this is string", hexstring1)
b64string = codecs.decode(hexstring1,"hex")
print("this is b64string", b64string)
print("\nChallenge 2\n")    
xor1 = '1c0111001f010100061a024b53535009181c'
xor2 = '686974207468652062756c6c277320657965'
print(codecs.encode(bxor(xor1,xor2),"hex"))
"""

#print("\nChallenge 3\n")

ch3hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def is_ascii(s):
    return all((ord(c) < 127 and ord(c) > 31) for c in s)
    
def spcount(st):
    a=0
    for c in st:
        if (ord(c)==32):
            a+=1 
    return a


def decrypt(inpt):
    for i in range(255):
        decoded = b""
        sDec = ""
        for b1 in codecs.decode(inpt,"hex"):
            decoded += bytes([b1 ^ i]) 
        try:
            if is_ascii(sDec):
                sDec = decoded.decode(encoding='UTF-8')
        except:
            pass
        if is_ascii(sDec) and spcount(sDec)>2: # Likely a sentence if there are more than 2 spaces
            print(sDec)
 
#decrypt(ch3hex)

# Challenge 4!!

print("\nChallenge 4\n")
"""
ch3hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print('Assessing :\n ' + ch3hex + '('+ str(len(ch3hex)) +')')
for i in range(255):
    likey1 = str(i)*len(ch3hex)
    #print('key:\n ' + likey1 + '(' + str(len(likey1)) + ')')
    xored = bxor(ch3hex,likey1)
    try:
        utf8xored = xored.decode(encoding='UTF-8')
        if is_ascii(utf8xored):
            print(utf8xored)
    except:
        pass
"""    

def count_spaces(st):
    a=0
    for c in st:
        if (c==' '):
            a+=1 
    return a 
    
with open('cryptopals4.txt', 'r') as c4f:
    for li in c4f.readlines():
        li=li.strip()
        print('Assessing : ' + li + '('+ str(len(li)) +')')
        for i in range(255):
            #likey1 = str(i)*len(li)
            #print('key:\n ' + likey1 + '(' + str(len(likey1)) + ')')
            #xored = bxor(li,i)
            xored = ""
            for m in range(len(li)):
                temp = ord(li[m]) ^ i
                if temp < 127 and temp > 31:    
                    if re.search("[0-9A-Za-z ]",chr(temp)):
                        xored += chr(temp)
            if len(xored)>20 and count_spaces(xored) > 2 and count_spaces(xored) <6 and re.search("the",xored):       
                print(xored) 

        
      
 
    
    
    
    
    
    
    
    
    
    
    

