# Lists are mutable, which means we can change their elements directly.
names = ["Samiksha","Sita","Ram"]
print(names[0])
print(names[-1])
print(len(names))

names[2]="Bhawana"
print(names)
names[-3]='Samii'
print(names)


# in list we can also do slicing like string. list is created using square brackets

numbers = [10,-20,10.5,0]
print(numbers[0:3])
print(numbers[:3])
print(numbers[0:])
print(numbers[0:3:2])
print(numbers[0:3:1])

# methods used in list
languages = ["Python","c","c++"]
languages.append("React")
print(languages)
languages.insert(1,"Java")
print(languages)
languages.remove("c++")
print(languages)
languages.pop(1)
print(languages)
languages.pop()
print(languages)

numberss = [10,30,40,5,0,1.1]
numberss.sort()
print(numberss)
numberss.sort(reverse=True)
print(numberss)
numberss.reverse()
print(numberss)


example = [10,20,30,40,10,10,10]
print(example.count(10))

language = ['java','python','c','c++']
print(language.index("c++"))
new_language = language.copy()
print(new_language)
print("python " in language)
print("c" in language)
