## integer ##
s = int(input("enter a number:"))
n= str(s)
print(n)

if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")

## string ##

s = input("enter a name:")
if (s==s[::-1]):
    print("palidrome")
else:
    print("not a palindrome")