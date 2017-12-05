Sequence Opeations Part1 & Part2: string, list & tuples are called as sequences. There are 10 sequence operators
in python as follows:
     1.LENGTH
     2.SLICE
     3.INDEX
     4.CONCATENATION
     5.MAX VALUE
     6.SELECT
     7.COUNT
     8.MEMBERSHIP
     9.MIN VALUE
     10.SUM

All these 10sequences can be applied to strings, list & tuples.
     
     
1.Length:
>>> name = 'Guido'
>>> list1 = ['guava', 'apple', 'grapes']
>>> tuple = ('Google', 'Facebook', 'Twitter', 'Microsoft')
>>> len(name)
5
>>> len(list1)
3
>>> len(tuple)
4

2.Select:If You want to select individual element from string, list & tuples. 'select' is useful.

>>> name[0]
'G'
>>> list1[1]
'apple'
>>> tuple[3]
'Microsoft'

3.Slice: If you want just part of the list, string or tuple. You can use slice feature.
>>> name[1:4]
'uid'
>>> list1[0:1]
['guava']
>>> tuple[0:2]
('Google', 'Facebook')
>>> tuple[:2]
('Google', 'Facebook')

4.count: if you want to count number of times that element is present in the string, list or tuple.
>>> name.count('u')
1
>>> list1.count('apple')
1
>>> tuple.count('Microsoft')
2

5.index: If you want to find out the index of any charactor,element. You can go for the index
operation.

>>> name
'Guido'
>>> name.index('G')
0
>>> list1
['guava', 'apple', 'grapes']
>>> list1.index('guava')
0
>>> tuple.index('Microsoft')
3

6.membership: As we have discussed, in/not in are membership operators. whether charactor
'G' is present in name or not. We will check this by  using 'in' operator.
>>> name
'Guido'
>>> 'G' in name
True
>>> 'G' not in name
False

7.concatenation: Used to concatenate strings, lists & tuples.
>>> name = 'Guido'
>>> s = 'Van Rossum'
>>> name + s
'GuidoVan Rossum'

>>> list2 = ['Hello', 2.5]
>>> list1 + list2
['guava', 'apple', 'grapes', 'Hello', 2.5]

>>> tuple2 = ('guio', 7.9)
>>> tuple + tuple2
('Google', 'Facebook', 'Twitter', 'Microsoft', 'Microsoft', 'guio', 7.9)

8.min value: When You want to find out minimum value of string, list & tuple.min value is used.
>>> min(name)
'G'
>>> min(list1)
'apple'
>>> min(tuple)
'Facebook'
>>> list1 = [7, 9.8, 4.5, 3.9, 12, 23]
>>> min(list1)
3.9
>>> min(tupple)
9.8

9. max value: That is the largest value present in the list, string or tuple.
>>> name
'Guido'
>>> max(name)
'u'
>>> list
<class 'list'>
>>> list1
[7, 9.8, 4.5, 3.9, 12, 23]
>>> max(list1)
23
>>> tupple
(23, 45, 9.8, 123)
>>> max(tupple)
123

10. sum: When You want to find out the total sum of the elements present in the list.sum is used.
>>> list1
[7, 9.8, 4.5, 3.9, 12, 23]
>>> sum(list1)
60.2
>>> tupple
(23, 45, 9.8, 123)
>>> sum(tupple)
200.8
note: We cant use some operations for strings. It gives error when used.
>>> sum(name)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    sum(name)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

These are the 10 sequences in Python. ThankYou.



