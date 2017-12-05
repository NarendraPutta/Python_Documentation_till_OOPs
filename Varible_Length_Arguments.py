Variable length arguments: Whenever we are defining any functions, We dont know
how many parameters are needed. In that case, We can use variable length arguments.

Example:

def func1(*mylist):
     for num in mylist:
          print(num)
     return

#main function

func1(10,20,30)
func1(2,3)
func1(1,2,3,4)

Output would be:
=================== RESTART: C:/Users/vinayb/Desktop/12.py ===================
10
20
30
2
3
1
2
3
4
>>> 

Absolute Ceil floor round & Trunc Numeric Functions: We have discussed many math
functions here. Please go through for the knowledge.

Absolute function: Absolute function will give the distance of the value from the Zero.
Some Examples:
>>> abs(5)
5
>>> abs(-6)
6
>>> abs(-9)
9

round function:
>>> round(3.7777779, 3)
3.778
>>> round(3.987659, 2)
3.99
>>> round(3.9876543, 4)
3.9877


Ceil function: Its a math function, To use this ceil function, We need to import a module.
That is import math. ceil, floor, Trunc module needs math module to be imported.

Ceil examples:
>>> import math
>>> math.ceil(4.8)
5
>>> math.ceil(5.8)
6
>>> math.ceil(7.1)
8
>>> math.ceil(-3.1)
-3
>>> math.ceil(-7.6)
-7
>>> math.ceil(-9.5)
-9
>>> math.floor(-9.1)
-10
>>> math.floor(-9.7)
-10
>>> math.floor(-8.7)
-9
>>> math.trunc(9.7)
9
>>> math.trunc(8.6)
8
>>> math.trunc(-9.5)
-9
>>> math.trunc(-12.98)
-12
>>> math.exp(5)
148.4131591025766
>>> math.e
2.718281828459045
>>> math.exp(4)
54.598150033144236
>>> math.e**4
54.59815003314423
>>> math.sqrt(4)
2.0
>>> math.sqrt(25)
5.0
>>> math.sqrt(36)
6.0
>>> max(10, 2.3, 4, 12)
12
>>> max(10, 2.7, 6.1, 9.8)
10
>>> min(10, 2.3, 4, 1)
1
>>> min(23, 12, 0, 12)
0
>>> math.modf(11)
(0.0, 11.0)
>>> math.modf(12.9991)
(0.9991000000000003, 12.0)
>>> math.modf(16.876)
(0.8760000000000012, 16.0)
>>> math.pow(3,4)
81.0
>>> math.pow(5,4)
625.0
>>> math.pow(9,8)
43046721.0
>>> math.pow(11,2)
121.0
>>> math.pi
3.141592653589793


