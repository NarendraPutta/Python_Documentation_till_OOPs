Identifiers, 
Keywords
Control Statements
Implicit & Explicit line joining.



Identifiers: Identifiers are nothing but these are names which are used in program.
example:
     i. Variable name(name = 'Python', Here name is called Identifier by which 'Python' is getting identified)
     ii. var_1 = 90
     iii._age = 30
Identifiers can contain letters, digits & _.
The First letter of the identifiers should start with Letter or underscore. Should not directly start with number
Special characters are also excluded in the variable names. Special characters give us the  errors. Examples given below
>>> 9 = 'Narendra'
SyntaxError: can't assign to literal
>>> $ = 'Python'
SyntaxError: invalid syntax
>>> 5var90 = 45
SyntaxError: invalid syntax


Keywords: Keywords are nothing but these are the words which have predefined meaning.
example, AND, OR, if, elif, else, while, for, def & so on. We cant use keywords as identifiers. If you try to use identifiers as keywords.Using keywords as identifiers would
give errors. To know more about keywords. Please type below command

>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import         return
True                elif                  in                  try
and                 else                 is                  while
as                  except              lambda         with
assert              finally             nonlocal       yield
break               for                  not                 
class               from                 or                  
continue        global              pass                


Control Characters:Control Characters are nothing but they control the Output.
Example: >>> print('Welcome \n\t to Videocon d2h \n \tLtd') would print as follows.
Welcome 
	 to Videocon d2h 
 	Ltd


Implicit & explicit line joining method: When we try to divide the input into different physical lines. It gives errors.
>>> print('hello
      
SyntaxError: EOL while scanning string literal

Implicit: The rule of the implicit line joining method,In the single line, number of the open quotes should be equivalent to close quotes. For Example:

>>> print('Hello'
      'Welcome')
HelloWelcome

Explicit Line joining Method: In this method, We are using the backslash(/) method to split the input.
>>> print('Hello \
Welcome to Videocon')
Hello Welcome to Videocon
