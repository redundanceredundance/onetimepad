# -*- coding: utf-8 -*-
"""
@author : sycramore
My implementation of the One Time Pad v1 to be used for plain text
planned version 2 to be used for encrypting files
"""
import os
import sys
import argparse


debug = True    #INFO: das machen viele benutzer wenn sie beim Entwickeln ausgaben möchten die später im programm nicht benötigt werden
                #meist irgendwelche zusätzliche Ausgaben (print) um den Programmfluss nachzuvollziehen

def parseArgs():
            parser = argparse.ArgumentParser(description='Encrypt or decrypt a file')
            parser.add_argument('--decrypt', action="store", dest="decryption", help='decrypt file')
            parser.add_argument('--encrypt', action="store", dest="encryption", help='encrypt file')
            parser.add_argument('--key', action="store", dest="key", metavar="KEYFILE", help='Decryption keyfile')
            #parser.add_argument('-o', action="store", dest="outfile", metavar="OUTPUTFILE", help='destination file')
            args = parser.parse_args()
            if (args.encryption is None and args.decryption is None):
                print("you must specify a if you would like to encrypt or decrypt, --encrypt source.file or --decrypt source.file")     #replaces the -i parameter
                exit(1)
            if (args.encryption is not None):
                if debug:
                    print "encrypting file"
                encrypt( open(args.encryption,"rb").read(), open(args.key,"rb").read() )
                

            if (args.decryption is not None):
                if debug:
                    print "decrypting file"
                decrypt( open(args.decryption,"rb").read(), open(args.key,"rb").read() )


def encrypt(plaintext, key):
    print "running encrypt function with parameter plaintext="+plaintext+" key="+key

def decrypt(cyphertext, key):
    print "running decrypt function with parameter cyphertext="+cyphertext+" key="+key
    
def converttobinary(input):
    binary = [bin(number)[2:] for number in input]
    return binary
    
def converttoascii(input):
    ascii = [ord(a) for a in input]
    return ascii
    
def converttostring(input):
    string = ''.join(str(h) for h in input)
    return string

def encryption(klartext2,schluessel2):
    for i in range(len(schluessel2)):
        cypher = int(klartext2[i] + schluessel2[i]) % 2
        geheimnis.append(cypher)
    return geheimnis
 
#generate key from random and export it as binary string
def generatekey(lenght):
    keyfromrandom = os.urandom(lenght)    
    writekey = open("generatedkey.txt", "w").write(keyfromrandom)
    binarykey = open("generatedkey.txt", "rb").read()
    return binarykey
    
    #kann sein, dass es hier noch probleme gibt. gibt os.urandom einen string oder eine liste aus?


#the program starts here:
parseArgs()
