def PrintNumbers(startNumber,maxNum,increment):
    x=startNumber
    while (x<maxNum):
        print(x)
        x+=increment

def SumOfList(list):
    sum=0
    for x in list:
        sum+=x
    return(sum)

def AverageOfList(list):
    sum=SumOfList(list)
    return sum/len(list)

'''    
print("prime numbers between 1 to 10000 are:")
PrintNumbers(1,10000,2)
print("multiples of 5 between 1 to 1000000")
PrintNumbers(5,10000,5)
'''
print("sum of list")
print(SumOfList([1, 2, 5, 10, 255, 3]))
print("average of list")
print(AverageOfList([1, 2, 5, 10, 255, 3]))
