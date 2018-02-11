# -*- coding: utf-8 -*-
"""
@author : sycramore
My implementation of the One Time Pad v1 to be used for plain text
planned version 2 to be used for encrypting files
Needs libary os
"""
import os
import sys
import argparse

#generate key from /dev/urandom
#write to fie generatedkey.txt
#return generated key for further encryption

inputfile = 'nullen.txt'
outputfile = ''
key = 'einsen.txt'
usage = 'hier muss noch text rein'
decryption = False
encryption = False
#parser = argparse.ArgumentParser()

#parser.add_argument("-d", "--decrypt", action="store_true", dest="decryption", default=False, help="Decrypt a chosen file")
#parser.add_argument("-e", "--encrypt", action="store_true", dest="encryption", default=False, help="Encrypt a chosen file")
#parser.add_argument("-i", action="store", type="string", dest="infile", metavar="INPUTFILE", default='', help="Input file for encryption or decryption")
#parser.add_argument("-k", action="store", type="string", dest="key", metavar="KEYFILE", default='', help="Decryption keyfile")
#parser.add_argument("-o", action="store", type="string", dest="outfile", metavar="OUTPUTFILE", default='', help="File name for output of encryption or decryption")

#args = parser.parse_args()
#decrypt = args.decryption
#encrypt = args.encryption
#infile  = args.infile
#outfile = args.outfile
#key = args.key

def converttobinary(input):
    binary = [bin(number)[2:] for number in input]
    return binary
    
def converttoascii(input):
    ascii = [ord(a) for a in input]
    return ascii
    
def converttostring(input):
    string = ''.join(str(h) for h in input)
    return string

#generate key from random and export it as binary string
def generatekey(lenght):
    keyfromrandom = os.urandom(lenght)    
    writekey = open("generatedkey.txt", "w").write(keyfromrandom)
    binarykey = open("generatedkey.txt", "rb").read()
    return binarykey
    
    #kann sein, dass es hier noch probleme gibt. gibt os.urandom einen string oder eine liste aus?

#nimmt liste mit buchstaben und wandelt sie in binaeren string um
#def convertinput(input):
#    asciiinput = converttoascii(input)
#    binaryinput = converttobinary(asciiinput)
#    stringbinaer = converttostring(binaryinput)
#    return stringbinaer
#Fallunterscheidung, Fall 1 Verschluesselung ohne vorhandenen Schluessel
#if (encrypt==True) and (key == ''):
kt = open(inputfile,"rb").read()

klartext = open(inputfile,"rb").read(len(kt)-1)
#laengeklartext = len(klartext)
#einfach das nicht benoetigte auskommentieren
generatedkey = generatekey((len(kt)-1)) #Schluessel muss 8 Mal so lang sein wie Klartext wegen Konversion Ascii zu binaer
print(generatedkey)
schluessel = open(key, "rb").read(len(klartext)) #lese soviele stellen vom key ein, wie klartext ziffern hat in binaer
ganzerschluessel = open(key, "rb").read()
key2 = open("key2.txt", "w").write(schluessel) #schreibe schluessel in textfile
komplementschluessel = ganzerschluessel[(len(klartext)-1):]
writenewkey = open("newkey.txt", "w").write(komplementschluessel) #speichere den neuen schluessel ab, also das komplement

listeklartext = [int(elem) for elem in list(klartext)]
print(listeklartext)
listeschluessel = [int(elem) for elem in list(schluessel)]
print(listeschluessel)


geheimnis = []
def encryption(klartext2,schluessel2):
    for i in range(len(schluessel2)):
        cypher = int(klartext2[i] + schluessel2[i]) % 2
        geheimnis.append(cypher)
    return geheimnis
 
cyphertext = encryption(listeklartext,listeschluessel)
print(cyphertext)

stringcyphertext = ''.join(str(h) for h in cyphertext)

cyphertextschreiben = open("cypher.txt","w").write(stringcyphertext)

#ab hier entschluesselung

cyphertextlesen = open("cypher.txt",'rb').read()
listecyphertext = [int(name) for name in cyphertextlesen]
print(listecyphertext)

#ab hier noch komische bugs drin
#warum klebt hier encryption cypher vor den klartext und oben nicht?
entschluesselterklartext = encryption(listecyphertext,listeschluessel)
print(entschluesselterklartext)
