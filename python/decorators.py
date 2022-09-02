
### Example 1:

def make_decorated(func):
    def inner_function():
        print("i got decorated")
        func()
    return inner_function

@make_decorated
def simple_func():
    print("i am a simple function")

#decor=make_decorated(simple_func)
#decor()

simple_func()

#### Example 2:

def smart_div(func):
    def inner_func(a,b):
        print("i am dividing",a,"and",b)
        if b == 0:
            print("oops! division by zero is illegal ... !")
            return
        return func(a,b)
    return inner_func
@smart_div
def go_divide(a,b):
    return a/b


print(go_divide(20,2))
print(go_divide(10,0))


### example 3

def hello_decorator(func):
    def inner1():
        print("hello, this is before execution")
        func()
        print("this is after function execution")
    return inner1

def function_to_be_used():
    print("this is inside the function !!")
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

