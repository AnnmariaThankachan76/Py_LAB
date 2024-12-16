
#string & numeric values can operate together with*
a,b=2,3
txt="$"
print(a*b*txt)


#string & string can operate with +
c,d="2",3
txt1="@"
print((c+txt1)*d)

#precedence
e,f=2,3
g=2
print(e+f*g)

#arithematic with float results in float
h,j=10,5.0
print(h+j)

#result of division operator with 2 integers will be float
x,y=12,4
print(x/y)

#integer division with float and int will give int displayed as float
v,u=13.0,5
w=v//u
print(w) 
z=v/u
print(z)
