range() function: In a nutshell, range() function generates list of numbers which is generally
used to iterate over with for loops. Often we will use range() when you want to perform
an action 'X' number of times.
#One Parameter
>>> for i in range(5):
	print(i)
0
1
2
3
4
#Two Parameters	
>>> for i in range(3,6):
	print(i)
3
4
5
#Going Backwards
>>> for i in range(0, -10, -2):
	print(i)
0
-2
-4
-6
-8

#Iterating lists:
>>> my_list = ['one', 'two', 'three', 'four', 'five']
>>> my_list_len = len(my_list)
>>> for i in range(0, my_list_len):
	print(my_list[i])
one
two
three
four
five

range() is also a continuous topic. I will cover it as & when it is required.
We will discuss about fuctions in the next tutorial.
