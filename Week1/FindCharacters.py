def FindCharacters(wordList,char):
    newList=[]
    for word in wordList:
        if (word.find(char)!=-1):
            newList.append(word)
    print(newList)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
FindCharacters(word_list,char)