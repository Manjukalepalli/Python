my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
myTuples=[]

for key in my_dict:
    myTuples.append((key,my_dict[key]))
    
print(myTuples)