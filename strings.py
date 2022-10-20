string = "Raahim"
print(string)
print(string[6])
print(len(string))
print(string[:])
print(string[-5:])
print('biryani' in string)
print('biryani' not in string)
string['m'] = 'l'
print(string)
string = string.replace('Raahim', 'icecream')
print(string)

print(dir(string))

print(string.endswith('l'))
print(string.isdecimal())
print(string.lower())
print(string.index('m'))

num = str(25)
s = 'my age is '
print(s + num)
print(type(num))

s = "Let's go for a walk"
print(s)

s = "My name is raahim\nand i study in karachi"
print(s)
s = "My name is raahim\tand i study in karachi"
print(s)    

name = 'Raahim'
age = 25
print("My name is", name, "and my age is", age)
print(f"My name is {name} and my age is {age}")
# # These are called as f strings

print("My name is {} and my age is {}".format(name, age))
