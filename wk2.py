# print(1)
#
# print(2)

# 1. Alt+Shift+E to run the specific line

# print('John said:"let\'s learn python together"') or use triple quotes

# division fo integer will give you floating number

# a=6/2
# print(a)

# a=0.2+0.2+0.2
# print(a==6)

# isclose from math library can check whetherr two values are close to each other

# import math
# a=0.2+0.2+0.2
# print(math.isclose(a,0.6))

# print(1==2)
# print(1==1)
# print(1=1)

# and: 两个都是true才是tue，其余都是false  or: 只要有一个是true就行

# print(1+2)
# print('3'+2)
# print(2+'3') 这两个error略有不同

# a=True
# b=5
# print(f"The value of a is {a} and the value of b is {b}")
# print("The value of a is {} and the value of b is {}".format(a,b))


# print(56*33*30.5)
# a=56
# b=33
# c=30.5
# print(a*b*c)

# length = 56
# width = 33
# height = 30.5
# volume = length*width*height
# print(f"the value of volume is {volume} cubic centimeters")

# append, extend, remove
# append:
# lst_a = [1]
# lst_a.append(2)
# print(lst_a)

# extend
# lst_a = [1]
# lst_b = [2, 3]
# lst_a.extend(lst_b)
# print(lst_a)

# remove:remove the first object in a list
# lst=[0,'string', True, None, True]
# lst.remove(True)
# print(f'lst after moving the first True is {lst} ')
#
# lst = [1, 'string', True, None, True]
# lst.remove(True)
# print(f'lst after moving the first True is {lst} ')
# 1 has same value as True, 0 has same value as False



# lst = [1, 'string', True, None, True]
# lst.pop()
# print(f'lst after moving the CURRENT last element is {lst}')
# pop(): remove the last object
# lst = [1, 'string', True, None, True]
# lst.pop(2)
# print(f'lst after moving the element currently at index 2 is {lst}')

# reverse
# lst= [1, 2, 3]
# lst.reverse()
# print(lst)

# line='welcome to the class'
# x=line.split()
# print(x)


# extract domain name
# line = 'From nickname.surname@unsw.edu.au Tue Oct 06:10:10：15 2020'
# domain = line.split()[1].split('@')[1]
# print(domain)

# tuple unpacking
# tuple=(1,2)
# (a,b)=tuple
# print(f'a is {a} and b is {b}')

# sets 不能有重复的object
# add，remove
# s={1,2,3}
# print(1 in s)

# dict
prc_dic = {
'2020-01-02':7.1600,
'2020-01-03':7.1900,
'2020-01-06':7.0000,
'2020-01-07':7.1000,
'2020-01-08':6.8600,
'2020-01-09':6.9500,
'2020-01-10':7.0000,
'2020-01-13':7.0200,
'2020-01-14':7.1100,
'2020-01-15':7.040,
}

# modify
prc_dic['2020-01-02']=1.000
print(prc_dic)
# add
prc_dic['2020-01-16']=6.92
print(prc_dic)

prc_dic.pop('2020-01-03')
print(f"After popping '2020-01-03'")











