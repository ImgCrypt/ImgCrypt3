import math
import random
def isChar(input):
    output = input.isalnum()
    #print(input)
    if not(output):
        output = (input in "\" \,(){}',.;'[])(*&^%$#@!   ?}|+-+_=-~`//><:;") or ((ord(input)> 31) and ord(input)>100)
    if not(output):
        output = ((input == chr(26)))
    if ord(input) == 127: output = False

    return output


def BinToArr(array):
    output = []
    for i in range(int(math.floor((len(array))/7))):
        output.append(array[i*7:(((i+1)*7))])
    output2 = []
    for i in output:
        output2.append(int(i,2))
    return(output2)


def ArrToBin(array):
    print("test"+NumToText(array))
    output = ""
    for i in array:
        new = (format(i, "b"))
        while len(new)<7:
            new = "0"+new
        if (len(new)==7) and isChar(NumToText(BinToArr(new))):

            output += new
    print("test2" + str(len(output)))
    return(output)



def TextToNum(text):
    output = []
    for i in text:
        if (len(format(ord(i),"b"))< 8) and (isChar(i)):
            output.append(ord(i))
    return output

def NumToText(num):
    text = ""
    for i in num:
        text = text+(chr(i))
        #print(chr(i))
    return text
breakchar = ArrToBin(TextToNum("[stop]"))#this is like a stop codon or something
def encode(img,msg):
    #print(len(breakchar))
    x = len(img[0])

    y = len(img)
    #msg = str(msg)[::-1]
    #msg = msg + breakchar
    mod = len(msg)%3
    pixels = math.ceil(len(msg)/3)
    lines = math.ceil(pixels/x)
    ticks = len(msg)
    brk = False
    for i in range(y):
        for ii in range(x-2):
            if not(brk):
                #print(y)

                for iii in range(3):

                    if not(img[i][ii][iii]%2 == int(msg[-ticks])):
                        if img[i][ii][iii] == 256:
                            img[i][ii][iii] = img[i][ii][iii] - 1
                        elif img[i][ii][iii] == 0:
                            img[i][ii][iii] = img[i][ii][iii] + 1
                        else:
                            if random.randint(1,2) == 1:
                                img[i][ii][iii] = img[i][ii][iii] + 1
                            else:
                                img[i][ii][iii] = img[i][ii][iii] - 1
                    ticks -=1
                    if ticks==0: brk=True
            else:
                #for iii in range(len(msg)%3):
                    #if not (img[i][ii][iii] % 2) == int(msg[(i * x + ii * 3 + iii)]):
                        #if img[i][ii][iii] == 256:
                           # img[i][ii][iii] = img[i][ii][iii] - 1
                        #elif img[i][ii][iii] == 0:
                           # img[i][ii][iii] = img[i][ii][iii] + 1
                        #else:
                            #if random.randint(1, 2) == 1:
                            #    img[i][ii][iii] = img[i][ii][iii] + 1
                            #else:
                            #    img[i][ii][iii] = img[i][ii][iii] - 1
                break
    print(img)
    return img


def decode(img,maxpixs):
    msg = ""
    end = False

    for i in range(len(img)):
        for ii in range(len(img[i])-2):
            if end:
                end = True
                break
            for iii in range(len(img[i][ii])):
                if ii+1 != len(img[i]) or True:
                    msg = msg + str(img[i][ii][iii]%2)
                if len(msg) % 7 == 0:
                    if ((not(isChar((NumToText(BinToArr(msg[-7:]))))) or end )) :
                        print((NumToText(BinToArr(msg[-7:]))))
                        print(((BinToArr(msg[-7:]))))
                        print(i)
                        end = True
                        break
    #print(msg)
    return msg

def hide_widget(wid,dohide):
    if hasattr(wid, 'saved_attrs'):
        if not dohide:
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
            #print(wid.height)
            del wid.saved_attrs
    elif dohide:
        wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
        wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True
