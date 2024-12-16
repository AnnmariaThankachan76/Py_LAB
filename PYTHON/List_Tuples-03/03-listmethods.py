'''list=[2,3,4]

list.append(8) # add an element at the end of a list 
print(list)


#sorting in ascending order
print(list.sort())
print(list)

#sorting in decending order
print(list.sort(reverse=True))
print(list)

#alphabatical sorting
list=["apple","orange","banana"]
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)

#complete reverse of the list
list=[2,3,4]
list.reverse()
print(list)
'''

#insert elemrnt in an index
list=[2,3,4,3]
list.insert(1,60)
list.insert(3,80)
print(list) # [2,60,3,80,4]

#removes first occurance of element
list.remove(3)
print(list) #[2,60,80,4,3]

#removes element at index
list.pop(3)
print(list) #[2,60,80,3]
