name = "samiksha"
print(type(name)) # it is used for finding the class

#string indexing
Name = "Samiksha"
print(Name[6])
print(Name[0])
print(Name[1])

# negative indexing
name1 = "samiksha"
print(name1[-8])
print(name[-1])

# basically indexing is used for geting one character
# slicing gets mulitple character

names = "Bhawana"
print(names[0:6])
print(names[0:4])
print(names[2:]) # starts from 2 till end
print(names[:5]) # starts from first to till 5
print(names[0:7:2]) # slicing with step
print(names[0:7:3]) #[start:end:step]
print(names[::-1]) # negative reverse
print(names[::1])
print(names[::-2])# goes backward and jump 2 steps
print(len(name)) # function used in string

# methods of string

word = "i love python  "
word1 ="        i love coding  "
print(word.upper())
print(word.lower())
print(word1.strip())
print(word.replace("love","loving"))
print(word.count("o"))
print(word.find("n"))
print(word.find("i"))
print(word.split())
print(word.capitalize())
print(names.startswith("Bha"))
print(names.endswith("ana"))
print(names.isalpha())

age = "23"
print(age.isdigit())

value = "Samiksha123"

print(value.isalnum())

first = "sami"
last = "siwakoti"
fullname = first +" "+last
print(fullname)

NAME = " python "
print(NAME * 3)

language = [" python "," Java "," c++ "]
result = "".join(language) # it is join function in python
print(result)

languages = [" python "," Java "," c++ "]
result = "-".join(language) # it is join function in python
print(result)


