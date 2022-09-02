#  number with in the range of prime number .

first = int(input("enter a first number :"))
second = int(input("enter a second number :"))
for i in range(first,second):
    for j in range(2,i//2):
        if i % j ==0:
            break
        else:
            print("prime number",i)