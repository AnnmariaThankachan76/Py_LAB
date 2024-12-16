#dictionaries are used to store data values in key:valuse pairs

dict={
  "name":"Pinapple",#string
  "age":20,
  "marks":91.21,
  "is_adult":True,
  "subjects":["python","c","Java"],#list
  "topics":("String","Pointers","Swing"),#tuple
  12:3444 # can use int,float,list as keys ,but not prefered


}
print(dict)
print(type(dict))

#dictionary are unordered
#mutable
#don't alllow duplicate keys


#extracting subjects only
print(dict["subjects"])

dict["name"]="Orange" #overwrite
print(dict)


