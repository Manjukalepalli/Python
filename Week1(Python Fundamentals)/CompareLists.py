def CompareLists(list_one,list_two):
    if(list_one==list_two):
        print('same')
    else:
        print('not same')


list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
CompareLists(list_one,list_two)
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
CompareLists(list_one,list_two)
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
CompareLists(list_one,list_two)
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
CompareLists(list_one,list_two)

