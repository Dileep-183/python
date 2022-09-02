# convert string into list,tuple,set .

s = "ganesh"
n = list(s)
print(n)

s = "sai"
n = tuple(s)
print(n)

s = "vivek"
n = set(s)
print(n)

# convert list,tuple,set to string.

s = [1,2,3,"sai",4.4,689]
n = str(s)
print(n)

s = (1,2,3,"sai",4.4,689)
n = str(s)
print(n)


s = {1,2,3,"sai",4.4,689}
n = str(s)
print(n)

# Reverse order.

s = int(input("enter a number:"))
n = str(s)
print(n)
print(n[::-1])

s = "ganesh"
print(s[::-1])


# positive / negative number

s = int(input("enter a number :"))
if s < 0:
    print("negative")
else:
    print("positive")


# odd / even number

num = int(input("enter a number:"))
if num % 2 ==0:
    print("even number")
else:
    print("odd number")


# leap year

year = int(input("enter a year:"))
if year % 4 == 0:
    print("leap year")
else:
    print("not leap year")


# swap number

x = 10
y = 20
print(x,y)
x,y = y,x
print(x,y)

# or #

x = int(input("enter a number:"))
y = int(input("enter a number:"))

temp = x
x = y
y = temp

print("x after is:{}".format(x))
print("y after is:{}".format(y))

# palindrome

#string palindrome #
s = input("enter:")
if (s==s[::-1]):
    print("palindrome")
else:
    print("not palindrome")

# integer palindrome #
i = int(input("enter:"))
n = str(i)
print(n)
if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")


# prime number

x = int(input("enter a number :"))
a= x%x
b= x%2
c= x%3
if x==3 or x==2:
    print("prime number")
else:
    if a==b or b==c:
        print("not prime number")
    else:
        print("prime number")


# seperate string and list from list.

names = []
numbers = []

l = ["dileep",123,"sai",456,"ganesh",789]

for i in l:
    if type(l)==str:
        names.append(i)
    if type(l)==int:
        numbers.append(i)
print(names,numbers)


# factorial number

num = 6
factorial = 1

if num <0:
    print("factorial doesn't exist with negative number")
elif num ==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
        print("factorial of",num,"is",factorial)


