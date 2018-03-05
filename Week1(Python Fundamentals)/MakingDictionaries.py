def new_dict(list1,list2):
    newDict ={'name':list1,'favorite_animal':list1}
    return newDict
    


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
newDict=new_dict(name,favorite_animal)
print(newDict['name'])
print(newDict['favorite_animal'])
