collection=set()
collection.add(33)
collection.add(567)
collection.add(90)
collection.add(10) 
#set is mutuble but elements are immutable
print(collection)

print("Removed 10")
collection.remove(10)
print(collection)

collection.add((1,2,3))#-> list 
print(collection)

'''collection.add([4,5,6]) #->list ,error
print(collection)'''

collection.clear() #clear the set into empty
print(collection)

collection1={"hello","hai","olla"}
print(collection1.pop()) #randomly pops any one elements

