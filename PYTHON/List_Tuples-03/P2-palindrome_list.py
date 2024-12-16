n1=(int)(input("Enter the first element of the list"))
n2=(int)(input("Enter the second element of the list"))
n3=(int)(input("Enter the third element of the list"))
n4=(int)(input("Enter the fourth element of the list"))
n5=(int)(input("Enter the fifth element of the list"))
list=[n1,n2,n3,n4,n5]
print("List in its original order")
print(list)
copy1_list=list.copy()
copy1_list.reverse()
print("List after reversing")
print(copy1_list)
if(list==copy1_list):
    print("Its palindrome")
else:
    print("Not palindrome")

#4.07.50