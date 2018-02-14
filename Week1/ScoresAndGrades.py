import random
def PrintGrades(marks):
    if (marks>=60 and marks<70):
        print('Score: '+str(marks)+'; Grade: '+'D')
    elif(marks>=70 and marks<80):
        print('Score: '+str(marks)+'; Grade: '+'C')
    elif (marks>=80 and marks<90):
        print('Score: '+str(marks)+'; Grade: '+'B')
    else:
        print('Score: '+str(marks)+'; Grade: '+'A')

i=1
while (i<=10):
    num= random.randint(60,100)
    PrintGrades(num)
    i+=1
        