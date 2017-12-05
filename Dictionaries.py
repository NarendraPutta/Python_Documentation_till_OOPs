9.2 covers more topics:
     Introduction to Dictionaries :
     More funtion examples:

Introduction to Dictionaries :
They are various ways to store the data in the system that is using file or folder.
But If the amount of data is very large. We cant use file or folder to use the data.
For that WE can go for the database and the softwares which are used in the database
are called database management system.
Before storing this data to database, We need to organize this data or we need to store the data
in particular format and this format is called as data structures.

We already discussed about th linear data structures. list & tuples are called linear
data structures where the data is stored in the linear order where we can access the data
using location or the index of the data.

There is another data structure called as assossiated data structure. In the assossiated data structure
we can access the data using key values.

dictionaries are one of the assossiated data structure. Now Lets discuss about dictionaries.

In the Python programming: dictionaries consist of key & values.
Dictionaries are mutable which means we can alter them whenever we want.
Now we will see how to create dictionaries & how to access the data from these
dictionaries.

 Additional Info: They can be changed in many ways.
Items can be removed from the dictionary with its assossiated with the Del Command.
A new value can be assossiated with a key by assigning a value to the key. Like So.

#Dictionaries : {KEY : VALUE}
#Example1:
>>> temp ={}
>>> temp['sun'] = 33.4
>>> temp['mon'] = 45
>>> temp['tue'] =30
>>> temp
{'sun': 33.4, 'mon': 45, 'tue': 30}

So, sun, mon, tue are keywords & 33.4, 45 and 30 are values.
keys and values are seperated by ':'
#Example2:
>>> mail_address
{'narendra': 'narendra@hotmail.com', 'naren': 'naren@gmail.com', 'nagini': 'nagini@yahoo.com'}
>>> mail_address.keys()
dict_keys(['narendra', 'naren', 'nagini'])
>>> mail_address.values()
dict_values(['narendra@hotmail.com', 'naren@gmail.com', 'nagini@yahoo.com'])
>>> mail_address['narendra']
'narendra@hotmail.com'
>>> mail_address['naren']
'naren@gmail.com'
>>> mail_address['nagini']
'nagini@yahoo.com'
#Example3: Another way
phone_book = {'Narendra' : '9599333748', 'Naren' : '9599333749'}
print(phone_book['Narendra'])
phone_book['Modi'] = '9999999999'
print(phone_book)
print(phone_book['Modi'])
del phone_book['Modi']
print(phone_book)

zoo_animals = {'Unicorn' : 'Cotton Candy House', 'sloth' : 'Rain Forest Exibit',
               'Bengal Tiger' : 'Jungle house', 'Atlantic Pufin' : 'Artic Exbit',
               'RockHopper Penguin' : 'Arctic Exhibit'}

del zoo_animal['Unicorn']
del zoo_animal['sloth']
del zoo_animal['Bengal Tiger']

Remove Few things: Sometimes You need to remove somethings from a list
remove = ['Me', 'Myself', 'I']
remove.remove('Myself')
print(remove)


Its Dangerous to go Alone! Take this:

inventory['Pocket'] =['SeaShell', 'Strange', 'Strange Berry', 'Lint']
inventory['BackPack'] = ['Xylophone', 'dagger', 'Bedroll', 'Breadloaf']
inventory['BackPack'].sort()
inventory['BackPack'].remove('dagger')
inventory['Gold'] = inventory['gold'] + 50

printing list names using for loop

names = ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']

for names in ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']:
     print(names)

You can use the forloop in the dictionaries also. Note that dictonaties are unordered.
Which means that any time you loop thru dictionary, You will go through every key.
But You are not guaranteed to get them in any particular order.


webster = {
     "Python": "Happening Language"
     "Perl" : " Happening, But difficult"
     "C" : "Mother of all"
     "Java" : "Cool Thing, But Big Syntaxes annoys people"
     "Ruby" : "Heard that its Good too, But I have no idea as of now"
     }

for item in webster:
     print(item)

Control_Flow & the Looping

a = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13]

for numbers in a:
     print(numbers)

numbers = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13]

for numbers in numbers:
     if number > 6:
          print(numbers)
print("We printed 7")

numbers = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13]

for numbers in numbers:
     if numbers %2 == 0:
          print(numbers)
print("We printed all the even numbers Because WE like Even Numbers")

LIST + Functions:

Functions also can take list as inputs and perform various operations on that list.

def count_small(numbers):
     total = 0
     for n in numbers:
          if n < 10:
               total = total + 1
     return total

listt = [4, 8, 15, 16, 23, 42]
small = count_small(listt)
print(small)


def fizz_count(x):
     count = 0
     for item in x:
          if x == 'fizz':
               count = count + 1
          return count
fizz_count(['fizz', 'cat', 'fizz'])
