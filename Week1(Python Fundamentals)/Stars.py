def PrintStars(list):
    for l in list:
        if (isinstance(l,int)):
            num=l
            p='*'
        else:
            p=l[0]
            num=len(l)
        s=BuildString(num,p)
        print(s)

def BuildString(num,p):
    i=1
    s=''
    while (i<=num):
        s+=p
        i+=1
    return s

PrintStars(['cat',5,6])