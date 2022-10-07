
string = "hello world"

for char in string:
    print(char , end=" ")

    ''''''


''''''
s = "hello"
d = {}

for char in s:
    d[char] = ord(char)
print(d , end =" ")

print()

''''''

''''''
s = "abracadabraca"
d = {}
for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char] = d[char]+1
print(d)
''''''
s = "hello world"
d = {}

for vow in s:
    if vow not in "aeiouAEIOU":
        if vow not in d:
            d[vow] = 1
        else:
            d[vow] = d[vow]+1

print(d)

""""""
#########################################################################
a = [1,2,3,4]
b = [5,6,7,8]

l = []
for index in range(len(a)):
    l.append(a[index] + b[index])
print(l)

''''''
names = ['apple','google','apple','yahoo','yahoo','facebook','apple','gmail','gmail','gmail','gmail']
d = { }

for char in names:
    if names.count(char) > 1 :
        d[char] = names.count(char)

print(d)

''''''
names = ['apple' , 'google', 'apple','yahoo' , 'yahoo', 'google' , 'gmail' , 'gmail','gmail']

for val in names:
    d[val]= [names.index(val)]
print(d)

print()
''''''

names = ['apple' , 'google', 'apple','yahoo' , 'yahoo', 'google' , 'gmail' , 'gmail','gmail']
d = {}
for index,val in enumerate(names):
    if val not in d:
        d[val]= [index]
    else:
        d[val].append(index)
print(d)

''''''

l = [10,20,30]
s = "hai"
for item in zip(l,s):
    print(item)

for element1,element2 in zip(l,s):
    print(element1 , element2)



