# CS177 -- padding oracle attacks This code is (unfortunately) meant
# to be run with Python 2.7.10 on the CSIL cluster
# machines. Unfortunately, cryptography libraries are not available
# for Python3 at present, it would seem.
from Crypto.Cipher import AES
import binascii
import sys

def check_enc(text):
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val == 0 or val > 16:
        return False

    for i in range(1,val+1):
        if (int(binascii.hexlify(text[nl-i]), 16) != val):
            return False
    return True
                                 
def PadOracle(ciphertext):
    if len(ciphertext) % 16 != 0:
        return False
    
    tkey = 'Sixteen byte key'

    ivd = ciphertext[:AES.block_size]
    dc = AES.new(tkey, AES.MODE_CBC, ivd)
    ptext = dc.decrypt(ciphertext[AES.block_size:])

    return check_enc(ptext)


# Padding-oracle attack comes here

if len(sys.argv) > 1:
    myfile = open(sys.argv[1], "r")
    ctext=myfile.read()
    myfile.close()

    # complete from here. The ciphertext is now (hopefully) stored in
    # ctext as a string. Individual symbols can be accessed as
    # int(ctext[i]). Some more hints will be given on the Piazza
    # page.
    
    #print("Original ciphertext:")
    #print(ctext)
    #print(PadOracle(ctext))
    textList = []
    temp = []
    plainList = []
    
    #hexText = ctext.encode("hex")
    #print(hexText)
    for c in ctext:
        intChar = ord(c)
        #print(hexChar)
        textList.append(intChar)
        temp.append(intChar)
        plainList.append(intChar)
    
    #print(plainList)
    size = len(textList)
    
    for t in range(16, size):
        #start here
        guess = []
        x = size - t - 1
        #print(x)
        target = (16 - x) % 16
        #print(target)
        #print(textList[x])
        
        #find guesses
        for g in range(0, 255):
            if g == textList[x]:
                pass
            replace = g ^ textList[x] ^ target
            temp[x] = replace
            
            #check guesses
            if target != 1:
                for i in range(1, target - 1):
                    temp[x - i] = plainList[x - i] ^ target ^ textList[x - i]
            tempText = ""
            
            #convert to ciphertext
            for n in range(0, size):
                tempText = tempText + chr(temp[n])
            
            #test guesses
            if(PadOracle(tempText)):
                guess.append(replace)
            #reset temp
            for q in range(0, size):
                temp[q] = textList[q]
                
        #print(guess)
        
        #verify guesses
        if target != 0:
            if len(guess) > 1:
                for y in range(0, len(guess)):
                    temp[x] = guess[y]
                    for i in range(1, target):
                        temp[x + i] = plainList[x + i] ^ target ^ textList[x + i]
                    if(temp[x - 1] != 1):
                        temp[x - 1] = 1
                    else:
                        temp[x - 1] == 2
                    
                    tempText = ""
                    for n in range(0, size):
                        tempText = tempText + chr(temp[n])
                    if PadOracle(tempText):
                        plainList[x] = guess[y]
                        break
            else:
                plainList[x] = guess[0]
                
        else:
            plainList[x] = guess[0]
        #insert correct guess
        
            
    #convert PlainList to plainText
    plainText = ""
    for n in range(0, size):
        plainText = plainText + chr(plainList[n])
    print(plainText)
    print("\n")
    # end completing here, leave rest unchanged.
else:
    print("You need to specify a file!")
    
