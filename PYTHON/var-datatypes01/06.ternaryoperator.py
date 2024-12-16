
'''print("Enter the food item")
food=input()
eat=  "yes" if food=="cake" else "no"
print(eat)

food1=input("food1 :")
print("sweet") if food=="cake" or food=="laddu" else print("not sweet")'''


#<var>=(false-val,true-val)[condition]
age=int(input("age :"))
vote=("yes","no")[age<18]
print(vote)

sal=float(input("salary :"))
tax=sal*(4.0,6.0)[sal<=100]
print(tax)