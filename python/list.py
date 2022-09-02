s = [1,2,3,4.5,"dileep"]
print(s)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
s.insert(5,10)
print(s)
s.append(33)        # add only single value at a time at the end of list.
print(s)
m = [10,20,30]      # add multiple list to single list or can add tuple,set,dict.
s.extend(m)
print(s)
s.insert(8,"ganesh")    # insert an item at the specified index.
print(s)
s.remove(10)            # remove required element in the list.
print(s)
s.pop(6)               # used to remove with index values.
print(s)
####     slicing  ###
print(s[:4])
print(s[2:])
print(s[2:4])
print(s[:])
print(s[::-1])             # reverse order
print(len(s))              # length of the list .
s.clear()                  # it is used to clear the entire list.
print(s)

###  Adding two list
d = ["vivek",45,67,"arun"]
print(s+d)
print(s)

### or ###
# list
a = [1,2,3,4,5,"radha"]
b = [6,7,8,9,10,"vivek"]
a.extend(b)
print(a,"list")

# adding tuple to list.
c = [11,22,33,44,55,"op"]
d = (66,77,88,99,100,"dileep")
c.extend(d)
print(c,"tuple")

# adding set to list.
a = [1,2,3,4,5,"radha"]
b = {6,7,8,9,10,"vivek"}
a.extend(b)
print(a,"set")

# adding dict to list.
a = {"name": "John", "age": 20}
b = []
c = a. copy()
b. append(c)
print(b,"dict")


### changing list inside list value.
x = [1,2,3,[4,5,6]]
for i in range(len(x)):
    if x[i]==[4,5,6]:
        x[i]=[2,5,6]
print(x)


### List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist,"List Comprehension")


### Sort List ###
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

## Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


