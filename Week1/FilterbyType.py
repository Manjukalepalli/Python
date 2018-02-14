def FindTypeAndPrintRange(x):
    if (isinstance(x,str)):
        LongOrShortString(x)
    elif (isinstance(x,int)):
        BigOrSmallInteger(x)
    elif (isinstance(x,list)):
        SmallOrBigList(x)

def LongOrShortString(x):
    if (len(x)>=50):
        print("Long sentence.")
    else:
        print("short sentence.")

def BigOrSmallInteger(x):
    if (x>=100):
         print("its a big number.")
    else:
        print("its a small number.")

def  SmallOrBigList(x):
    if (len(x)>=10):
        print("big list")
    else:
        print("small list")


FindTypeAndPrintRange(45)
FindTypeAndPrintRange(100)
FindTypeAndPrintRange(455)
FindTypeAndPrintRange(0)
FindTypeAndPrintRange(-23)
FindTypeAndPrintRange("Rubber baby buggy bumpers")
FindTypeAndPrintRange("Experience is simply the name we give our mistakes")
FindTypeAndPrintRange("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
FindTypeAndPrintRange("")
FindTypeAndPrintRange([1,7,4,21])
FindTypeAndPrintRange([3,5,7,34,3,2,113,65,8,89])
FindTypeAndPrintRange([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
FindTypeAndPrintRange([])
FindTypeAndPrintRange(['name','address','phone number','social security number'])
