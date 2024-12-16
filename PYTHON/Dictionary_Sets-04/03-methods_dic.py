student={
  "name":"Annmaria",
  "subject":{
    "physics":87,
    "chemistry":98,
    "math":87}
}
print(student)
print("Printing only keys")
print(student.keys()) #.keys -to print the keys of dictionary

print("Type casting into list")
print(list(student.keys()))

#length of the dictionary
print(len(student))

print(student.values()) #show the values
print((list)(student.values())) #type cast to list

print(student.items()) #pairs in tuple form

# to print in pairs

pairs=list(student.items())
print("Printing in pairs")
print(pairs[0])

#returns the key according to value
print("getting the value")
print(student.get("name"))

'''print(student["name2"])#error
print(student.get["name2])# error but shows->none'''


student.update({"city":"delhi"})
new_dic={"Interesed areas":"maths","age":39}
student.update(new_dic)
print(student)
