names = []
numbers = []

s = ["dileep",123,"sai",456,"ganesh",789]
for i in s:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i)
print(names,numbers)
