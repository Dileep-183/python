x = int(input("enter any number :"))
a = x%x
b = x%2
c = x%3
if (x==2) or (x==3):
    print("prime number")
else:
    if a==b or a==c:
        print("not prime")
    else:
        print("prime")



## program to print all prime number in given number ##

lower = 900
upper = 1000

for num in range(lower,upper+1):    # num == 900
    if num>1:
        for i in range(2,num):      # i====2
            if num % i ==0:
                break
        else:
            print(num)




