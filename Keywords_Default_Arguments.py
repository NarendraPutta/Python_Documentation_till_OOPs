Keyword & Default Arguments:
#Program to calculate the average of 3numbers:
def average(n1, n2, n3):
     return (n1 + n2 + n3)/3.0    #Function Definition
print('Welcome')
num1 = int(input())
num2 = int(input())
num3 = int(input())

result = average(num1, num2, num3)  #Function Call

print(result)

formal parameters & actual parameters names can be different.
The position of the parameters matters but not the name of the parameter.
Using different name in the function definition & function call is acceptable

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Welcome
10
20
30
20.0
>>> 

Now Lets discuss about the keyword arguments
#Above program slightly in different method

def average(n1, n2, n3):
     return (n1 + n2 + n3)/3.0    #Function Definition
print('Welcome')
result = average(n2 =5, n1=19, n3=21)  #Function Call

print(result)

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Welcome
15.0
>>> 

When You observe, result = average(n2 =5, n1=19, n3=21), First we have defined n2, then
n1 followed by n3 values. In this case it is not based on the position. Its based on the keyword.

Here Python provides the option to use the keyword argumentst that is instead of the positional
argument, We can use the parameter name and can declare the value.

By using the keyword arguments, We can change the position of the parameters. This is
about the keyword arguments.

Next We can use default arguments also.

Take another example now:

def average(n1, n2, n3=5):
     return (n1 + n2 + n3)/3.0    #Function Definition
print('Welcome')
num1 = int(input())
num2 = int(input())
num3 = int(input())

result = average(num1, num2, num3)  #Function Call

print(result)

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Welcome
12
12
13
12.333333333333334

Here when you observed above program, here n3 =5. But asked the user to enter the value
for num3 also. num3 will take the value as 3 and performs the operation.

Another way of running the program is: If we want,We can remove the 

def average(n1, n2, n3=5):
     return (n1 + n2 + n3)/3.0    #Function Definition
print('Welcome')
num1 = int(input())
num2 = int(input())
#num3 = int(input())

result = average(num1, num2)  #Function Call

print(result)

Output would be
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Welcome
12
12
9.666666666666666
>>> 
Output would be 9.66. Here 12 and 12. num1 value is 12 and num2 value is 20. We will
call the average fuction(12,12). In the formal parameters n1 is replaced with 12 and n2
is also replaced with 12. n3 by default taken as 5 and it will perform the operations.
This is called as default arguments.

