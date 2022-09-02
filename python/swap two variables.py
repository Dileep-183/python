x = input("enter a value of x: ")
y = input("enter a value of y: ")

# create a temporary variable and swap the values #
temp = x
x= y
y = temp

print("the value of x after swaping:{}".format(x))
print("the value of y after swaping:{}".format(y))


## or ###

x,y = 10,20
print(x,y)
x,y = y,x
print(x,y)
