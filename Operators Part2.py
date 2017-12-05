Arthemetic Operators & Relational Operators:

     ARITHEMETIC OPERATORS:
          1. Negation
          2. Addition
          3.Subtraction
          4.Multiplication
          5.Division
          6.Truncating div
          7.Modulus
          8.Exponential

     
Membership Operators:
     in
     not in

Boolean Operators:
     and
     or
     not

Identity Operators:
     is
     is not
     

1.Negation: Negation is an Unary operator which is used to negate the value for example
Example:
>>> -5
-5
2.Addition: '+' Symbol is used for Addition.
Example:
>>> 5 + 6
11
3.Substraction: '-' Symbol is used for Subtraction.
Example:
>>> 5 -3
2
4.Multiplication: '*' is used to Multiply the Numbers
>>> 6 * 6
36
5.Division: ''/' is used to divide the Numbers
>>> 25/5
5.0
6.Truncating Division: It is similar to the Division. But It truncates the results.For Example
in the case of 5/4 answer is 1.25 if we use truncating the division.
>>> 5//4
1
Here Answer is 1 it will eliminate the digits which are present after the point.
7.Modulus: Modulus will give the reminder as the results for example 5%2. Here
'%' symbol is used as Modulus Symbol
>>> 5 % 2
1
8.Exponential: If you want to find out the answer for 2 power 5 here 2 is called as Base
and 5 is called as Exponent. If you want to find out the exponential of some value then You can use
exponential operator. '**' Symbol is used for the Exponential
>>> 2(Base) ** 5(Exponential)
32


Relation Operators: There are 6types of Relational Operators in the Relational Operators.
'==' equal to: This is used to check whether two elements are equal or not equal.
>>> 5 == 5
True
'!='   not equal to : This is used to check whether two elements are equal or not equal.
>>> 5 != 5
False     
'>'greater than:greater than is used to check whether the left element is greater than the right element or nor.
>>> 10>5
True
'>=' greater than or equal to: This is the combination of greater than or equals to operator.
>>> 10>=5
True
'<'less than : Less than is used to check whether the left element is less than the right element or nor.
>>> 10<5
False
'<='  less than or equal to: This is the combination of less than or equals to operator.
>>> 5<=5
True
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Membership Operators:There are two membership operators are used to check whether the given element is member of group elements. We will take some examples for better understanding.
     in : I will take one element that is 5 and I will use membership operator in.Now We will check whether 5 is present in the group of element or not. Here I will use List. List of one of the fundemental concepts of Python Programming.
     List is nothing but these are the group of some elements. I will type 2,3,6,7,5,9 and now we are checking whether 5 the there in the group of element or not.
     Example:>>> 5 in [2,3,4,5,7]
                              True (We can see True here because 5 is there in the List and we are getting result as True)
     not in: Not in exactly opposite of in: which means it will check whether the element is present, It will give answer as false if its not present,  It will give answer as true.
          >>> 5 not in [2,3,4,5,6,7]
                         False(Here result will be false because 5 is present in the list)

Boolean Operators:
     and : If both the operands are true then condition becomes true. (a and b) is true
     or: If any of the two operands are non-zero then condition becomes true. (a or b) is true.
     not:Used to reverse the logical state of its operand. Not(a and b) is false.

Identity Operators:
     Identity operators compare the memory locations of two objects. There are two Identity operators as explained below

Operator  Description Example
is	Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. x is y, here is results in 1 if id(x) equals id(y).
is not	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. x is not y, here is not results in 1 if id(x) is not equal to id(y).
Example:
a = 20
b = 20

if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"

if ( id(a) == id(b) ):
   print "Line 2 - a and b have same identity"
else:
   print "Line 2 - a and b do not have same identity"

b = 30
if ( a is b ):
   print "Line 3 - a and b have same identity"
else:
   print "Line 3 - a and b do not have same identity"

if ( a is not b ):
   print "Line 4 - a and b do not have same identity"
else:
   print "Line 4 - a and b have same identity"
          






          
     











