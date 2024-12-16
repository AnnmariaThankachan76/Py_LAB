tuple=(1,4,9,16,25,36,49,64,81,100)
print(tuple)
x=int(input("Enter a number to be searched in the tuple"))
i=0
while i<len(tuple):
  if(tuple[i]==x):
    print("Yes ,",x," is found in the tuple")
    break
  i+=1