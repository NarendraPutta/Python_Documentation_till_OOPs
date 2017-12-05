Iterative Control:Iterative control statements repeatedly execute the instructions so these are
also reffered as loops. That is below for statement is called for loop & while statement is also
called while loop.
     for statement
     while statement

for loop syntax:
     for variable in sequence:
          action

sequence is nothing but it can be list or strings. strings are nothing but values which are
enclosed with in a single quote or double quotes and list is a group of diffrent types of
values.

#Example 01 for for loop: string

for letter in "Python":
     print('Charactor is', letter)

Output would be
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
Charactor is P
Charactor is y
Charactor is t
Charactor is h
Charactor is o
Charactor is n

As We discussed, for is an iterative control statement that is this will execute instruction
repeatedly. In the above example letter is a variable here first charactor will be assigned
to variable letter.
So, letter is equal to p now when it is executed for the first time again the control goes
to the for loop and now letter is y. So, it will execute statements again control goes & so on.

#Example 02 for for loop: list
for letter in [10,20,30,40]:
     print(letter)

Output would be
============ RESTART: C:\Users\vinayb\Desktop\DESKTOP\Practice.py ============
10
20
30
40
--------
We can use if else or if statement in the for loop. That is here as follows.

#Example 03 for loop:
for letter in [10,20,30,40]:
     if letter >=25:
          print(letter, 'Greater than 25')
     else:
          print(letter, 'less than 25')

Explanation: In the above program, There are list of elements that is 10,20,30,40.In the if
statement we checked whether the value is greater than equals to 25. If it is greater than
equals to 25. then we printed 'greater than 25' message. if it is not then we will go for
else part.


Study drill:
     Please help me to prepare this document further:
	 continue document preparation with all the for loop cases I have given it to you  & submit the document back to me. Please let me know if you need any assistance: ThankYou
 
 # ForLoop to print basic Pyramid Pattern

num = int(input('Enter the number of rows: '))
for i in range(1, num +1):
     for j in range(1, i+1):
          print('5', end=' ')
     print()

print('*************************************************************************************************')


#2 stars increment in each line

num = int(input('Enter the Number of rows: '))
k=1
for i in range(1,num+1):
     for j in range(1, k+1):
          print('*', end=' ')
     k = k+2
     print('     ')


print('*************************************************************************************************') ''



 #Print stars in the pyramid shape
num = int(input('Enter the number of row: '))
for i in range(0,num):
     for j in range(0,num-i-1):
          print(end=' ')
     for j in range(0, i+1):
          print('*', end=' ')
     print()

print('*************************************************************************************************')




#Reverse Pyramid shape
num = int(input("Enter the number of rows: "))
for i in range(num, 0, -1):
     for j in range(0, num-i):
          print(end=' ')
     for j in range(0,i):
          print('*', end=' ')
     print()

print('*************************************************************************************************')



#Dimond Shape
def pyramid(rows):
     for i in range(rows):
          print(' '*(rows-i-1)+'* '*(i+1))
     for j in range(rows-1,0,-1):
          print(' '*(rows-j)+'* '*(j))'''

 '''#Print A

for row in range(7):
     for col in range(5):
          if((col==0 or col==4) and row !=0) or ((row == 0 or row ==3) and (col>0 and col<4)):
               print('*', end='')
          else:
               print(end=' ')
     print()

print('*************************************************************************************************')


# print B

for row in range(7):
   for col in range(5):      
        if(col==0 or col == 4) or ((row==0 or row ==3 or row ==6) and (col>0 and col <4)):
         print("*",end="")
        else:
         print(end=" ")
   print ()

print('*************************************************************************************************') ''


#Print E

for row in range(7):
   for col in range(5):
        if col == 0 or ((row == 0 or row==3 or row ==6) and (col>0)):
             print('*', end=' ')
        else:
            print(end=' ')
   print()


print('*************************************************************************************************') ''

val=65
for i in range(0,5):
      for j in range(0,i+1):
           ch=chr(val)
           print(ch,end=' ')
      val=val+1
      print()
 print('*************************************************************************************************') ''

num=1
for i in range(0,5):
     for j in range(5,i,-1):
          print(num,end=' ')
          num=num+1
     print()
     num=1

print('*************************************************************************************************') ''

fibonacci=[0,1,1,2,3,5,8,13,21]
for i in range(len(fibonacci)):
     print(i,fibonacci[i])
print()

print('*************************************************************************************************') ''

val=65
for i in range(0,5):
     for j in range(0,i+1):
          ch=chr(val)
          print(ch,end=' ')
          val=val+1
     print()

print('*************************************************************************************************') ''

num=int(input('Enter the number of rows'))
n=1
for i in range(0,num):
     for j in range(0,i+1):
          print(n,end=' ')
     n=n+1
     print()


*********************************************************************************************************************************OUTPUT*********************************************************************************************************ForLoop to print basic Pyramid Pattern
>>> #ForLoop to print basic Pyramid Pattern
Enter the number of rows: 5
* 
* * 
* * * 
* * * * 
* * * * *

>>> #2 stars increment in each line
Enter the Number of rows: 6
*      
* * *      
* * * * *      
* * * * * * *      
* * * * * * * * *      
* * * * * * * * * * *

>>>#Print stars in the pyramid shape
Enter the number of row: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * *

>>>#Reverse Pyramid shape
Enter the number of rows: 6
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 



>>>#Print A
 *** 
*   *
*   *
*****
*   *
*   *
*   *

>>># print B
*****
*   *
*   *
*****
*   *
*   *
*****

#Print E
* * * * * 
*     
*     
* * * * * 
*     
*     
* * * * * 


         
A 
B B 
C C C 
D D D D 
E E E E E    
     
     


1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


    
0 0
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21


A 
B C 
D E F 
G H I J 
K L M N O     



Enter the number of rows5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 





