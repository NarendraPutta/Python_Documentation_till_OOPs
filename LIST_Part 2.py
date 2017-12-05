List and List Type:

example#1: animals = []  # Square brackets indicate lists.
>>> animals = []
>>> animals
[]
>>> animals = ['dog', 'cat', 'monkey']
>>> animals[0]
'dog'
>>> animals[1]
'cat'
#Example 2:
>>> my_list1 = [5, 12, 13, 14] # the list contains all integer values  
>>> print(my_list1)
#Example 3:
[5, 12, 13, 14]  
>>> my_list2 = ['red', 'blue', 'black', 'white'] # the list contains all string  
values  
>>> print(my_list2)
#Example4
['red', 'blue', 'black', 'white']  
>>> my_list3 = ['red', 12, 112.12] # the list contains a string, an integer and  
a float values  
>>> print(my_list3)  
['red', 12, 112.12]  
>>>  

#Example 6:
>>> color_list1 = ["White", "Yellow"]  
>>> color_list2 = ["Red", "Blue"]  
>>> color_list3 = ["Green", "Black"]  
>>> color_list = color_list1 + color_list2 + color_list3  
>>> print(color_list)  
['White', 'Yellow', 'Red', 'Blue', 'Green', 'Black']  
>>> number = [1,2,3]  
>>> print(number[0]*4)  
4  
>>> print(number*4)  
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]  


#Example 7:
list1 = [10, 23.2, 'Guido', 54] 
print(list1)

#Example 8: List within the List: For more info, Please refer to the Bahubali lists examples which I have shared with you few weeks back & pactice.
>>> list2 = [[10,20], [34, 'Hello']]
>>> list2
[[10, 20], [34, 'Hello']]
>>> list2[0]
[10, 20]
>>> list2[0:1]
[[10, 20]]
>>> print(list2[0][0])
10

#Program
for num in [10,20,45,'Guido']:
     print(num)

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
10
20
45
Guido
>>> 

Thats all in this sessions,. We will discuss about List operations in the next class.
