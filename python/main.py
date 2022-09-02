### VARIABLE
#  storing some data in container is variable #
# age = 20
# print(age)
# name = "dileep"
# print(name)
# a=5
# b=6
# c=a+b
# print(c)

### type conversion ###

# name = str(input("enter your name:"))
# print(name)
#
# year = int(input("enter your year:"))
# age = 2020 - year
# print(age)


### string ###

# name = "Chitturi sri sai Dileep"
# print(name.upper())
# print(name.lower())
# print(name.find('D'))
# print(name.find("sri"))
# print(name.replace('Dileep',"dhoni"))
# print('Dileep' in name)


### Arthematic Operations ###

# a = 5
# b = 3
# add = a+b
# sub = a-b
# mul = a*b
# div = a/b
# module = a%b
# power = a**b
# print(add)
# print(sub)
# print(mul)
# print(div)
# print(module)
# print(power)


### Operator Precedence ###

# x = 10 + 3 * 2
# print(x)
# y = (10 + 3) * 2
# print(y)

### Comparsion Operator ###

#    > , < , >= , <= , == , !=

### Logical Operator ###

# And , Or , Not

# price = 25
# print(price > 10 and price <30)
## if both operation are correct it is true or it is false

## Or ##
# if any one Operator is correct it is true.
#
# price = 25
# print(price > 10 or price < 25)

## Not ##
# it will inverse
#
# price = 5
# print(not price > 10)


### If Else ###

# temperature = 35
#
# if temperature > 40:
#     print("it is a hot day")
#     print("drink plenty of water")
# elif temperature > 20:
#     print("it is a nice day")
# else:
#     print("It is very cool")


## While Loop ###

# i = 1
# while i <=10:
#     print(i)
#     i = i+1

## for Loop ###

# num = [1,2,3,4,5]
# for i in num:
#     print(i)

### Range ###

# for i in range(0,11):
#     print(i)
# for i in range(0,11,2):
#     print(i)


### Lists ###

# s = [1,2,3,'dileep',4.5,3,79]
# print(s[2])
# print(s[-2])
# print(s[0:])
# print(s[:6])
# print(s[:-1])
# s[5] = 6
# print(s)
# s.insert(2,33)
# print(s)
# s.append("ganesh")
# print(s)
# s.remove(33)
# print(s)

### Tuple ###

# tup = ("apple", "banana", "cherry", "apple")
# print(tup)
# print(tup[1])
# print(len(tup))
#
# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)


### set ###
# it does not have indexing and does not duplicate.

# s = {9,8,7,3,21,1}
# print(s)


### dictionary ###

# dic = {1:"dileep",2:"ganesh",3:"sai",4:"radha"}
# print(dic.keys())
# print(dic.values())
# print(dic[1])
# dic[1] = "kumar"
# print(dic)

### Array is nothing but combination of list,tuple,set,dict.
### Array is mothername.


###  Imp Questions ###
# int -> array
# array -> int
# array -> string
# string -> array
# int -> string
# string -> int


### convert list into string ###
s = [1,2,3,4,5]
lis = "".join(map(str,s))
print(lis)

### convert tuples into string ###
d =(4,56,"dileep",8,5.5)
m="".join(map(str,d))
print(m)

### convert sets into string ###
d ={4,56,"sai",8,5.5}
m="".join(map(str,d))
print(m)

### convert int to list ###
s = 34
n = str(s)
print(n)
f = list(n)
print(f)

s = 7
n = str(s)
print(n)
f = list(n)
print(f)

### convert int to tuple ###

s = 456789
n = str(s)
print(n)
f = tuple(n)
print(f)

### convert int to set ###

s = 456789
n = str(s)
print(n)
f = set(n)
print(f)


### convert string to integer ###

s = "98765434"
j = int(s)
print(j)

### convert string to list ###

s = "dileep"
m = list(s)
print(m)





