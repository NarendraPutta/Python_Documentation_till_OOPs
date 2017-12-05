Precedence & Assiociativity:

Precedence: First We will discuss about Precedence. We will take up one example where you want to
add 2numbers that is 2 + 5 then You want to multiply this results with 4. That is 2 + 5
answer is 7 then You want to multiply that 7 with 4 and I will press enter.2+5=7 and &
7*4 = 28.

We were expenting answer as 28.But we got answer as 22 as shown below.
>>> 2+5*4
22

This is because while evaluating an expression which contains multiple operator we need
to follow rule of priority than others. That is some operators have highest priority than
others.

In the Above example, There are 2 symbols '+' and '*' Here '*' has highest priority than
'+'. So, here 5 * 4 will evaluated first that is 20 then this result is added to 2 So, We are getting
answer as '22'

This Rule of priority is called precedence. Precedence is used while evaluating an expression
which contains multiple operator.

Python Operators Precedence
The following table lists all operators from highest precedence to lowest.

[ Show Example ]

Operator	Description
()                        Braces
**	            Exponentiation (raise to the power)
+ -	            Complement, unary plus and minus (method names for the last two are +@ and -@)
* / % //	              Multiply, divide, modulo and floor division
+ -	            Addition and subtraction
>> <<	            Right and left bitwise shift
&	            Bitwise 'AND'	
^ |	            Bitwise exclusive `OR' and regular `OR'
<= < > >=           Comparison operators
<> == !=	            Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not	            Identity operators
in not in	            Membership operators
not or and          Logical operators


Assosiativity: If an expression contains multiple operators, which has same precedence then how to evaluate that?
For example: 2+5-1 in this expression '+' and '-' has the same precedence. So, We cant apply the rule.  Here we cant apply rule of priority.
So, In this case, We can  apply assossiativity rule,
There are two types of assossiativity that is left to right evaluation & the second one is right to left evaluation.
All Most all the operators follow left to right evaluation. that is
2+5-1: In the left to right evalution: first 2+5 is evaluated, then '-' wil be evaluated. Output would be
>>> 2+5-1
6
But exponential case is right to left. Ex: 2 ** 3 ** 4
>>> 2 ** 3 ** 4 (Right to Left)
2417851639229258349412352



