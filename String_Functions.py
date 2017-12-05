String functions:
Please go through the examples & You will the idea about the string functions
that are being used. I have not explained theory over here as the document gets Unnecessary
length.
You will get it very easily when we discuss it.

i.String Functions capitalize count abd endswith
ii.Functions find length split and title
iii.Functions lower, upper, islower, isupper
iv.String functions replace isdigit & isalpha
v.Functions strip, Istrip, rstrip

>>> string = "Hello Welcome to Python Class"
>>> string = "hello Welcome to Python Class"
>>> string
'hello Welcome to Python Class'
>>> string.capitalize()
'Hello welcome to python class'
>>> string1 = "Welcome to Videocon"
>>> string1
'Welcome to Videocon'
>>> string1.capitalize()
'Welcome to videocon'
>>> str1 = """ Johnny Jonny Yes papa
eating sugar no papa
telling lied no papa
open your mouth hahahahah """
>>> str1
' Johnny Jonny Yes papa\neating sugar no papa\ntelling lied no papa\nopen your mouth hahahahah '
>>> str1.count('no')
2
>>> str1.count('papa')
3
>>> str1.count('sugar')
1
>>> str2 = 'Google.com'
>>> str2.endswith('com')
True
>>> str2.endswith('m')
True
>>> str2.endswith('org')
False

Functions find length split and title:
>>> str1 = 'amuls academy'
>>> str1
'amuls academy'
>>> str1.find('y')
12
>>> str1.find('academy')
6
>>> str1.find('ca')
7
>>> len(str1)
13
>>> str1.split()
['amuls', 'academy']
>>> str2 = 'Hello Welcome to Videocon Company'
>>> str2.split()
['Hello', 'Welcome', 'to', 'Videocon', 'Company']
>>> str2.split('o')
['Hell', ' Welc', 'me t', ' Vide', 'c', 'n C', 'mpany']
>>> str2.title()
'Hello Welcome To Videocon Company'
Functions lower, upper, islower, isupper:
>>> str1 = 'Guido Van Rossum'
>>> str1.lower()
'guido van rossum'
>>> str2 = 'BILL STEVE JOBS GATES'
>>> str2.lower()
'bill steve jobs gates'
>>> str3 = 'WELCOME TO BOARD'
>>> srt3.lower()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    srt3.lower()
NameError: name 'srt3' is not defined
>>> str3.lower()
'welcome to board'
>>> str3.islower()
False
>>> str1.islower()
False
>>> str2.islower()
False
>>> str4 = 'narendra'
>>> str4.islower()
True
>>> str4
'narendra'
>>> str4.upper()
'NARENDRA'
>>> st4.isupper()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    st4.isupper()
NameError: name 'st4' is not defined
>>> str4.upper()
'NARENDRA'
>>> str4.isupper()
False
>>> str5 = 'Sunder Pichai'
>>> str5.isupper()
False
>>> str1 = 'Hello World'
>>> str1.swapcase()
'hELLO wORLD'
>>> str2 = 'Chalo World'
>>> str2.swapcase()
'cHALO wORLD'
>>> str5 = 'Narendra Modi'
>>> str1.isdigit()
False
>>> str6 = '123456'
>>> str6.isdigit()
True
>>> str7 = '12345r'
>>> str7.isalpha()
False
>>> st7.isalpha()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    st7.isalpha()
NameError: name 'st7' is not defined
>>> str7.isalpha()
False
>>> str1
'Hello Welcome Nisha. You have a good name'
>>> str1.isalpha()
False
>>> str8 = 'HELLOBOLO'
>>> str8.isalpha()
True
>>> str1 = '!!!!!Hello!!!!!'
>>> str1.strip('!')
'Hello'
>>> str1.strip('$')
' What are you upto'
>>> str2 = 'Im upto completing part 8 Python Tutorial@@@@@'
>>> str2.strip('@')
'Im upto completing part 8 Python Tutorial'
>>> str1.strip('!')
'HELLO'
>>> str1 = '$$$ What are you upto'
>>> str1.strip('$')
' What are you upto'
>>> str2 = 'Im upto completing part 8 Python Tutorial@@@@@'
>>> str2.strip('@')
'Im upto completing part 8 Python Tutorial'
>>> str3 = '!!!Guido Van Rossum Invented Python!!!'
>>> str3.lstrip('!')
'Guido Van Rossum Invented Python!!!'
>>> str3.rstrip('!')
'!!!Guido Van Rossum Invented Python'
>>> str4 = '!!!hi strip, You are very useful sometimes in solving the real world problems!!!'
>>> str4.strip('!')
'hi strip, You are very useful sometimes in solving the real world problems'


