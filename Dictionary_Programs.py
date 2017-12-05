dictionary Operations: We can create dictionaries in other way.
>>> dict()
{}
>>> num =  {1: 'one', 2 : 'two', 3:'three'}
>>> num
{1: 'one', 2: 'two', 3: 'three'}
>>> numbers = dict(num)
>>> numbers
{1: 'one', 2: 'two', 3: 'three'}
>>> len(num)
3
>>> del num[2]
>>> num
{1: 'one', 3: 'three'}
>>> 1 in num
True
>>> 2 in num
False

Lists vs Dictionaries: In the Python programming, Lists & dictionaries are two
fundemental concepts. now we will discuss the difference between lists & dictionaries.

As we already know list is the linear data structure and dictionary is an assossiated data
structure.

In the list: We use index values to derive actual values where as in the dictionary using
the key values, we can derive the actual values.

>>> list1 = [2,3,4,'Hello', 'Hi', 'Bolo']
>>> list1[3]
'Hello'
>>> dict1 = {1: 'one', 2:'two', 3:'three'}
>>> dict1[2]
'two'
>>> 

#Temperature display program using list

daily_temps = [68.8, 71, 67, 71.8, 73.4, 75.5, 75]

day = input("Enter 'sun', 'mon', 'tue', 'wed', 'thurs', 'fri' or 'sat': ")

if day == 'sun' :
     dayname = 'sunday'
     temp = daily_temps[0]

elif day == 'mon' :
     dayname = 'monday'
     temp = daily_temps[1]

elif day == 'tue':
     dayname = 'tuesday'
     temp = daily_temps[2]

elif day == 'wed' :
     dayname = 'wednesday'
     temp = daily_temps[3]

elif day == 'thurs:
     dayname = 'thursday'
     temp = daily_temps[4]

elif day == 'fri':
     dayname = 'friday'
     temp = daily_temps[5]

elif day == 'sat':
     dayname = 'saturday'
     temp = daily_temps[6]

else:
     print('Wrong Input')

print("The Temparature for: ", dayname, "was", temp, "degrees")


#Temparature Display Program using dictionaries

daily_temps = {'sun' : 68.8, 'mon' : 71, 'tues' : 67, 'wed' : 71.8, 'thur': 73.4, 'fri': 75.5, 'sat': 75}
dayname = {'sun' : 'sunday', 'mon': 'monday', 'tues' : 'tuesday', 'wed' : 'wednesday','thur':'thursday', 'fri':'friday', 'sat':'saturday'}
day = input("Enter 'sun', 'mon', 'tue', 'wed', 'thurs', 'fri' or 'sat': ")
print("The Temparature for: ", dayname[day], "was", daily_temps[day], "degrees")



