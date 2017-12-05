List Operators:There are 6list operations as follows:
     1.replace
     2.delete
     3.insert
     4.append
     5.sort
     6.reverse

We will discuss & try to understand one by one.

1. Replace: Whenever You want to alter the values in the list can be done by using the
replace operations.

>>> list1 = [10,20,45,67]
>>> Now We want to replace 2nd element 45 with 63
>>> list1[2] = 63
>>> list1
[10, 20, 63, 67]

2. Insert: Mention the index value that you want to insert & type the value that you want to insert.
>>> list1
[10, 20, 63, 67]
>>> list1.insert(2, 'Guido')
>>> list1
[10, 20, 'Guido', 63, 67]

3.sort: sort operations are used if the list contains similar values that is if is it containing
only numbers. If it contains only strings, Then also we can use sort operations.
But we cant use when different operators are present in the list & using gives error as follows.
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'str' and 'int'

#String sort example
>>> smartconnect = ['facebook', 'apps', 'mediaplayer', 'd2honline', 'SD']
>>> smartconnect.sort()
>>> smartconnect
['SD', 'apps', 'd2honline', 'facebook', 'mediaplayer']


#number Example: In the case of numbers, sort takes it as in ascending order.
>>> list2 = [10, 34, 11, 2.3, 56.7]
>>> list2.sort()
>>> list2
[2.3, 10, 11, 34, 56.7]

4. delete: When You want to delete some elements from the list. then you can use delete.
>>> list2
[2.3, 10, 11, 34, 56.7]
>>> del list2[2]
>>> list2
[2.3, 10, 34, 56.7]

You can delete whole list also by del list2
>>> del list2
>>> list2 #Gives error because list2 is already deleted.
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list2
NameError: name 'list2' is not defined

5.append: whenever you want to add the value at the end of the list, then append operation
will be useful.
>>> companies = ['Google', 'Facebook', 'Twitter', 'Microsoft']
>>> companies
['Google', 'Facebook', 'Twitter', 'Microsoft']
>>> companies.append('Whatsapp')
>>> companies
['Google', 'Facebook', 'Twitter', 'Microsoft', 'Whatsapp']

6.reverse: It is used to reverse the element present in the list.
>>> companies
['Google', 'Facebook', 'Twitter', 'Microsoft', 'Whatsapp']
>>> companies.reverse()
>>> comapanies
['Whatsapp', 'Microsoft', 'Twitter', 'Facebook', 'Google']

#Lets have one program where all the list operations are used.

fruits = ['apple', 'banana']
print(fruits)

fruits[1] = 'grapes' #replace
print(fruits)

fruits.insert(0, 'guava') #insert
print(fruits)

fruits.sort() #insert
print(fruits)

del fruits[0] #delete
print(fruits)

fruits.append('aloevera') #append
print(fruits)

fruits.reverse() # reverse
print(fruits)

Output would be

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
['apple', 'banana']
['apple', 'grapes']
['guava', 'apple', 'grapes']
['apple', 'grapes', 'guava']
['grapes', 'guava']
['grapes', 'guava', 'aloevera']
['aloevera', 'guava', 'grapes']





