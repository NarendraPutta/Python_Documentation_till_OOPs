Updating Global variables:

var = 10
def func1():
     var = var + 1
     print('Variable Value is', var)
     return

#main
func1()

This program would result following error.
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Traceback (most recent call last):
  File "C:\Users\vinayb\Desktop\DESKTOP\Practice.py", line 8, in <module>
    func1()
  File "C:\Users\vinayb\Desktop\DESKTOP\Practice.py", line 3, in func1
    var = var + 1
UnboundLocalError: local variable 'var' referenced before assignment
>>> 
We encounter above error because you are calling the the variable before declaring it &
It will not take by default variable which are assinged globally. So, the solution to such
cases is given below.

var = 10
def func1():
     global var #Mention 'global' before the variable,  so, that it can take it from the outside the function & use it.
     var = var + 1
     print('Variable Value is', var)
     return

#main
func1()

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Variable Value is 11
>>> 

function calling using strings:
# Function definition is here
def printme( str ):
      print str
      return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
I'm first call to user defined function!
Again second call to the same function

Pass by reference vs value
All parameters (arguments) in the Python language are passed by reference.
It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.
For example:-

# Function definition is here
def changeme(mylist):
     mylist.append([1,2,3,4]);
     print("Values inside the function: ", mylist)
     return

mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]
>>> 

# Function definition is here
def changeme( mylist ):
     mylist = [1,2,3,4]; # This would assign new reference in mylist
     print("Values inside the function: ", mylist)
     return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

The output would be
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]
>>> 




