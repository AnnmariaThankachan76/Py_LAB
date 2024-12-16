values={9,9.0}
print(values)# both values are same so ->{9}

values1={9,"9.0"}
print(values1) #->{9.'9.0'}

#using tuple
values2={
  (float,9.0),
  (int,9)
}
print(values2)