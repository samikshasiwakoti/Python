# set uses curly braces {}
# it is a collection of unique values.
# it is unordered
numbers = {10,20,20,20,10,30}
print(type(numbers))
print(numbers)
numbers.add(50)
print(numbers)
numbers.remove(50)
print(numbers)
print(len(numbers))
print(numbers.pop())
numbers.discard(20)
print(numbers)
numbers.add(10)
print(numbers)

# set operations
python_students = {"Samiksha","Samii","Ram"}
django_students = {"Samiksha","sita","Ram"}
print(python_students|django_students)
print(python_students & django_students)
print(python_students - django_students)
print(python_students ^ django_students)

empty = set()
print(type(empty))