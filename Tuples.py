Tuples: Tuples are similar to the list that is these are the group of different type
of elements. The different between list & tuple is list is mutable that is we can alter the list
whenever we want but once we create the tuple. We can alter it.
So, tuple is immutable.

tuple =() #tuples are identified by paranthesis
#empty tuple
num = () #Here num is an empty tuple.
#tuple assignment
>>> companies = ('Google', 'Facebook', 'Twitter', 'Microsoft')
>>> companies
('Google', 'Facebook', 'Twitter', 'Microsoft')
>>> companies[0]
'Google'
#Nested tuples
>>> tuple1
((10, 2.3), (25, 2.3))
>>> tuple1[0]
(10, 2.3)
>>> tuple1[0][0]
10

Note: Since tuples are immutable, We cant insert any element, delete any element, replace
any element in the tuple. If we take these operations in the tuple wud give error.
>>> companies.sort()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    companies.sort()
AttributeError: 'tuple' object has no attribute 'sort'

So, there are no operators in the tuples.

This is it for Python programming in tuples. meet you in next class.

