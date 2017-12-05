Loop controls break and continue: In some situations You want to come out of the
loop before completing the loop or You want to skip the part of the loop and execute the
next statement.
It can be possible using loop control statements that is break and continue.

break: break statement will terminate the current loop and it will continue the execution of
of next statement.

#Example 1
count = 0
while count <=5:
     if count == 3:
          break
     else:
          print(count)
     count = count + 1
print('ThankYou')

Output would be:
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
0
1
2
ThankYou

#Example2:

for letter in 'Python':
     if letter == 'n':
          break
     else:
          print(letter)
print('ThankYou')

============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
P
y
t
h
o
ThankYou
This is it about the break statement & Now lets move to continue statement

#Example3:
x = 0;  
s = 0  
while (x < 10):  
     s = s + x  
     x = x + 1  
else :  
     print('The sum of first 9 integers : ',s)

#Example 4:
x = 1;  
s = 0  
while (x < 10):  
     s = s + x  
     x = x + 1  
     if (x == 5):  
          break  
else :  
     print('The sum of first 9 integers : ',s)          
print('The sum of ',x,' numbers is :',s)  

continue:continue is use to skip the part of the loop.
#Example 5

for letter in 'Guido van Rossum':
     if letter == 'n':
          continue
     else:
          print(letter)
print('ThankYou')

#Example 6:

var = 10
while var > 0:
     var = var -1
     if var ==3:
          continue
     print(var)
print('ThankYou')

When 3==3, the control will go back to the beginning of the while loop. here 3 > 0 is true
so, 3-1 =2 and 2 == 3 is false will print 2 followed by subsequent code.

#Example7:
for x in range(6):  
    if (x == 3 or x==6):  
        continue  
    print(x)


