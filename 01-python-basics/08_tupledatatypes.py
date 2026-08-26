names = ('samiksha',20,90.5,True,10,10)
print(names)
print(type(names))
# indexing is same like string and lists
print(names[0])
print(names[1])
print(names[-1])

# it also support slicing like list and string
print(names[1:3])

#but it cant be changed after they are created
# names[1]='ram'
# print(names) this cant be changed 

print(len(names))
print(names.count(10))
print(names.index("samiksha"))

# in tuple there will not be reverse,remove,pop,sort,append in tuple
# tuple mainly support count and index

number = (10)
print(type(number)) # basically this is int , parenthess only doesnt make tuple

number1 = (10,) # this is tuple because there is comma
print(type(number1))

student = ('samiksha',20,80)
name,age,marks = student
print(name)
print(age)
print(marks)

# tuple can also written without paranthess
students = "samiksha",10.5,10,"true",[10,20,30]
print(type(students))
students[4].append(50)
print(students)


