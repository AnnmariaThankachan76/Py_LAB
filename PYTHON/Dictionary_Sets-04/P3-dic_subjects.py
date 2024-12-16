marks={} #empty dictionary
print(type(dict))

marks["chem"]=56
marks["phy"]=78
marks["maths"]=91
x=int(input("Enter the marks od biology :"))
marks.update({"bio": x})

print(marks)