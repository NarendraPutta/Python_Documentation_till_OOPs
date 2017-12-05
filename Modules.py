Modules: Modules are nothing but these are group of some instructions or functions
or statements.

for example: math module. math is the module in which different types of mathematical
functions are defined. To use all those functions, We need to import module called math.

One more advantage of module is sometimes we use some functions repeatedly in our
program. 

To use any module in our program. We need to use import as follows.

>>> import math
>>> math.factorial(4)
24 #Output.


Above function helped us  writing the whole factorial program in a single line.
If you wan to see how many functions are defined in the math module.you can see it
by giving following command.

>>> help(math)
Help on built-in module math:

Above command would give you all the functions available in the math module.
Im  not poviding here because document becomes lengthy. Please type in the console
check yourself. You will understand easily.

There are two types of modules. One is built-in module & another one is user-defined
module.
math function is built in module.

User defined module: To use user defined module. We have to write code in our program
and save it in a file.
Note: By default all the python modules are 
>>> import sys
>>> sys.path
['', 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\idlelib',
 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\lib',
 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36',
 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages']

Lets create one simple Program:
def module1():
     name = input('Please enter your name: ')
     print('Hello', name)
     return
You need to save it @ 'C:\\Users\\narendra\\AppData\\Local\\Programs\\Python\\Python36'
>>>import myModule1
>>> myModule1.module1()
Please enter your name: Narendra
Hello Narendra

That is how we can write our own modules also in Python language. But defined module
should be always present/saved in the 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\idlelib'

Lets save the module somewhere on the desktop & see how the module runs.
>>> import myModule1
>>> myModule1.module2()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    myModule1.module2()
AttributeError: module 'myModule1' has no attribute 'module2'

Running the program gives above mentioned error. So, ensure that your modules are always
saved in the 'C:\\Users\\vinayb\\AppData\\Local\\Programs\\Python\\Python36'

