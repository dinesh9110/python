# global variable
# variables declared outside function that can be acessed both in function and outside function

x="awesome"

def myfunc():
    print("python is"+x)

myfunc()

"""if you create a variable with the same name inside a function , this variable will be local and 
can be used inside the function."""


"""
x="awesome"
def myfunc():
    x="fantastic"
    print("python is"+x)
myfunc()
print("python is "+x)
"""