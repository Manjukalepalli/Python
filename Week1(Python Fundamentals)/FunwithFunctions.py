'''
def PrintOddOrEven(maxnumber):
    i=1
    while (i<=maxnumber):
        if (i%2!=0):
            print('Number is '+str(i)+'. This is an odd number')
        else:
            print('Number is '+str(i)+'. This is an even number')
        i+=1

PrintOddOrEven(5)
'''
def multiply(NumList,multiple):
    newList=[]
    for num in NumList:
        newList.append(num*multiple)
    return newList

p=multiply([2,4,10,16],5)
print(p)    

def layered_multiples(arr):
    new_array=[]
    for num in arr:
        i=1
        sub_arr=[]
        while (i<=num):
            sub_arr.append(1)
            i+=1
        new_array.append(sub_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print(x)