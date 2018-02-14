print("Find and Replace")
words = "It's thanksgiving day. It's my birthday,too!"
print("index of 'day' in '"+words+"' is: "+ str(words.find("day")))
newWords=words.replace("day","month")
print("'Day' wors is replaced with 'month': " +newWords)
print("Min and Max")
x = [2,54,-2,7,12,98]
print("max value in the list is: "+str(max(x)))
print("Min value in the list is: "+str(min(x)))
print("First and Last")
y = ["hello",2,54,-2,7,12,98,"world"]
print("First element in list: "+str(y[0]))
print("Last element in list: "+str(y[len(y)-1]))
print("New List")
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z=sorted(z)
print("sorted list is:"+str(z))
mid=round(len(z)/2)
print(mid)
newList=[]
newList.append(z[0:mid-1])
newList.extend(z[mid-1:len(z)])
print("new list is: "+ str(newList))

