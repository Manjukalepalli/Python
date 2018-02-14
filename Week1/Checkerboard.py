def Checkerboard(i):
    checkerSize=i
    while(i>0):
        string=''
        j=checkerSize
        while(j>0):
            if (i%2==0):
                string+='* '
            else:
                string+=' *'
            j-=2
        print(string)
        i-=1

Checkerboard(8)

