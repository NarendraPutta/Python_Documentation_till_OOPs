Local and Global variables: Local variables are variables used in given function. Other functions
cant use that variable. But Global functions can be used by any function.

#Example for Local Variable:

def func1():
     n = 5
     print('n value is', n)

def func2():
     n = 10
     print('n value is', n)
     func1()

#main
func2()

Output would be
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
n value is 10
n value is 5
>>> 

#Example for Global Variable:

n = 10
def func1():
     print('n value is', n)

def func2():
     print('n value is', n)     
     func1()

#main
func2()

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
n value is 10
n value is 10
>>> 

n = 10
def func1():
     print('n value is', n)

def func2():
     n = 35
     print('n value is', n)     
     func1()

#main
func2()


============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
n value is 35
n value is 10
>>> 

You will get it better during the explanation. Explanation would become very lengthy which
is not useful & required.
