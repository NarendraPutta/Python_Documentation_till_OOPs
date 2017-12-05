Functions:You’re already familiar with the print(), input(), and len() functions from the
previous chapters.Python provides several builtin functions like these, but you can also
write your own functions. A function is like a mini program within the program.functons are
nothing but these are the number of statements group together to do some particular task

To better understand how functions work, let’s create one. Type this program into the file editor and save it as helloFunc.py:
#Example 1
def is the keyword by which functions are identified.

def names():
     print('Python')
     print('Google')
     print('Microsoft')
     print('Guio Van Rossum')
     print('Automate the boring stuff')

names()
names()
names()

Explanation of the Program:
def names():The first line is a def statement , which defines a function named names().
     print('Python')
     print('Google')
     print('Microsoft')
     print('Guio Van Rossum')
     print('Automate the boring stuff')
The Code in the block that follows def statement is the body of the function. This code is
executed when the function is called. not when the function is defined.

When the program execution reached these calls. It will jump to the top line in the
function. the execution returns to the line that called the function and continues moving
through the code as before.

In the above program, the function is called 3times. Hence the code in the hello()
function is executed three times. & Output would be when you run the program:

names()
names()
names()

the names() after the function is called functions calls. In code the function call is jus the
function name followed by parantheses(). As of now. This knowledge is enough, We will
discuss as we progress in the course.

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Python
Google
Microsoft
Guio Van Rossum
Automate the boring stuff
Python
Google
Microsoft
Guio Van Rossum
Automate the boring stuff
Python
Google
Microsoft
Guio Van Rossum
Automate the boring stuff

#Example: 2 def Statements with Parameters

When you call the print() or len() function, you pass in values, called arguments in this context,
by typing them between the parentheses. You can also define your own functions that accept arguments.
Type this example into the file editor and save it as helloFunc2.py:
❶ def hello(name):
❷     print('Hello ' + name)

❸ hello('Alice')
  hello('Bob')
When you run this program, the output looks like this:
Hello Alice
Hello Bob

The definition of the hello() function in this program has a parameter called name ❶. A parameter is a variable that an argument is stored in when a function is called.
The first time the hello() function is called, it’s with the argument 'Alice' 
The program execution enters the function, and the variable name is automatically set to 'Alice', which is what gets printed by the print() statement ❷.

One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns. For example,
if you added print(name) after hello('Bob') in the previous program, the program would give you a 
NameError because there is no variable named name. This variable was destroyed after the function call hello('Bob') had returned,
so print(name) would refer to a name variable that does not exist.

This is similar to how a program’s variables are forgotten when the program terminates. I’ll talk more about why that happens later in the chapter, when I discuss what a function’s local scope is.

#Example: 3: def Statements with Parameters
def average(n1, n2, n3):
     return (n1 + n2 + n3)/3.0
print('finally welcome to functions')
result1 = average(10,20,30)   # Function Call
results2 = average(1,2,3)
results3 = average(3.1,1.2,4.5)

print(result1)
print(results2)
print(results3)

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
finally welcome to functions
20.0
2.0
2.9333333333333336

It takes so much explanation & lead to heavy documentation. I will explain you so, that You will get it easily.
http://www.pythontutor.com/live.html#mode=edit
#This site Helps you understand how the code is running line after line.
     
