Function Types, actual & formal parameters:

We will take  the 6.1 example again for the explanation:
#Program to calculate the average of 3numbers:
def average(n1, n2, n3):
     return (n1 + n2 + n3)/3.0    #Function Definition
print('finally welcome to functions')
result1 = average(10,20,30)   # Function Call
results2 = average(1,2,3)
results3 = average(3.1,1.2,4.5)

print(result1)
print(results2)
print(results3)


Function Definition:
def average(n1, n2, n3):
     return (n1 + n2 + n3)/3.0

The Parameters(n1,n2,n3) which are used inside the function is called formal parameters.


function call: The Parameters which are called in the function call are called actual parameters.
result1 = average(10,20,30)   # Function Call
results2 = average(1,2,3)
results3 = average(3.1,1.2,4.5)

When the actual parameters(ie: 10,20,30) in the function call are passed to the(n1+n2+n3)
This entire concept is called positional arguments.

Whenever the function is called, it performs (n1 + n2 + n3)/3.0  and result will return & it
will store in the variable(ie:result1). When we go to print(result1), We can see the output

So, These are called value returning functions.

There are someother types of functions which will not return any value. Those functions
are called non-value returning functions.

Example:

def display():
     print('Welcome')
     print('Have a nice day')

display()

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Welcome
Have a nice day
>>> 

Here this function is not returning any value. This types of functions are called non-returning
functions.



