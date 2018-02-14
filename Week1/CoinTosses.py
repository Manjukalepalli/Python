import random

def CountHeadOrTail():
    i=1
    headCount=0
    tailCount=0
    print('Starting the program...')
    while(i<=10):
        num=random.randint(0,1)
        if (round(num)==0):
            tailCount+=1
            print('Attempt #'+str(i)+': throwing a coin...its a tail!... Got '+str(headCount)+' head (s) so far and '+str(tailCount)+' tail(s) so far')
        else:
            headCount+=1
            print('Attempt #'+str(i)+': throwing a coin...its a head!... Got '+str(headCount)+' head (s) so far and '+str(tailCount)+' tail(s) so far')
        i+=1

CountHeadOrTail()
