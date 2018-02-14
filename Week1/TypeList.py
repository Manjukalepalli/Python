def TypeList(givenList):
    tot=0
    string=""
    for l in givenList:
        if (isinstance(l,str)):
            string+=l
        elif (isinstance(l,int)):
            tot+=l

    if(len(string)==0 and tot!=0):
        print("The list you entered is of integer type")
        print("Sum: "+str(tot))
    elif (tot==0 and len(string)!=0):
        print("The list you entered is of string type")
        print("srting: "+string)
    elif (tot!=0 and len(string)!=0):
        print("The list you entered is of mixed type")
        print("string: "+string)
        print("sum: ",str(tot))
    else:
        print("The list you entered is empty")

TypeList(['magical unicorns',19,'hello',98.98,'world'])
TypeList([2,3,1,7,4,12])
TypeList(['magical','unicorns'])
TypeList([])