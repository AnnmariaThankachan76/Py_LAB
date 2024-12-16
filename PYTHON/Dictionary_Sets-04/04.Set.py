#set is the collection of the unordered items
#Each element in the set must be unique & immutable


#list and dictonary cannot be used in sets because
#they are mutuble 

set1={1,2,3,4}
print(set1)
print(type(set1))

set2={1,2,3,2,2,"world","world"}
print(set2) #deplicate of values are removed automatically

print(len(set1)) #-> 4
print(len(set2)) #->4 ,no duplicates are valid


collection=set() #empty set
print(type(collection))