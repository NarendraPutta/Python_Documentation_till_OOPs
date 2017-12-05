We will following topics in this session:
     1.List Assignment & Copying:
     2.range() function

Assignment list:
>>> list1
[7, 9.8, 4.5, 3.9, 12, 23]
>>> list2
[7, 9.8, 4.5, 3.9, 12, 23]
>>> list1[0] = 'Guido'
>>> list1
['Guido', 9.8, 4.5, 3.9, 12, 23]
>>> list2
['Guido', 9.8, 4.5, 3.9, 12, 23]

copying the list:we will use list() constructor. list() is called list constructor & It is helpful to
create the copy of the list.
>>> list1
['Guido', 9.8, 4.5, 3.9, 12, 23]
>>> list3 = list(list1)
>>> list3
['Guido', 9.8, 4.5, 3.9, 12, 23]

>>> list1[0] = 0
>>> list1
[0, 9.8, 4.5, 3.9, 12, 23]
>>> list3
['Guido', 9.8, 4.5, 3.9, 12, 23]

Now while creating the list. We will different types of values within the square brackets.
instead of values, We can genearate the statements which will generate the values.

>>> result = [x**2 for x in [1,2,3]
	  ]
>>> result
[1, 4, 9]

>>> result = [x**3 for x in [4,7,9]]
>>> result
[64, 343, 729]


