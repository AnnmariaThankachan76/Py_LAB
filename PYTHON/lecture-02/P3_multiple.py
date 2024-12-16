num=int(input("Enter a number to check whrther it is a multiple of 5 or 7 or 10 : "))
if(num%5==0):
    print(num," is divisible by 5")
elif(num%7==0):
    print(num," is divisible by 7")
elif(num%10==0):
    print(num," is divisible by 10")
else:
    print("Not divisible by 5,7,10")