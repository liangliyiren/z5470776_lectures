lst1=['a']
lst2=['a',lst1]
lst3=['b',['a']]

print(lst1)
print(lst2)
print(lst3)
#
lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}")
print(f"This is lst1 after modifying lst2: {lst1}")

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")

print(f"This is lst1 after modifying lst3: {lst1}")

happy = True
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = False
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = 55
if happy:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = ['a']
if happy:
    print("I am happy")
print("This will print regardless of the value of happy")

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

var1 == var2
var1 is var2

print(var1)
print(var2)

print(id(var1))
print(id(var2))

a = -1
b = True
if a != 0:
 print("a is non-zero")
elif b is True:
 print("b is True")
elif a < 0 and b is True:
 print("a is negative and b is True")
else:
 print("None of the conditions above hold")
 # execute the first satisfied condition

happy = True
if happy is True:
    pass

happy = True
if happy is True


name = input('Who are you?')
print('Welcome to the class,', name)




