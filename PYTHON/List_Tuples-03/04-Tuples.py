#list mutable
#tuples are imutable like strings

tup=(2,3,4)
print(type(tup))
print(tup[2])
'''tup[0]=5  error as tuple is immutable'''

#empty tuple
tup=()
print(tup)

tup=(1,)
print(tup) #is a tuple
tup=(1)
print(tup) #is an integer