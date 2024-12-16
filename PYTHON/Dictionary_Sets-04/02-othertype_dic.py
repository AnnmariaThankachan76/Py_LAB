nulldict={}
print(nulldict)#null dictionary

nulldict["name"]="karan"
print(nulldict) #added one element to it


#nested dictionary
student={
  "name":"Annmaria",
  "subject":{
    "physics":87,
    "chemistry":98,
    "math":87}
}
print(student)

print("Marks of chemistry ")
print(student["subject"]["physics"])