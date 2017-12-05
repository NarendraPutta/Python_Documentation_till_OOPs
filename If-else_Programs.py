if-else Statements

if else: If else statements are used when user wants two choices. That is when condition
is true, It peforms some action and when condition is false. It performs someother action.
Lets have some example1:
num = 3
if num > 0:
     print(num, "is a positive number.")
     print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
    print("This is also always printed.")

Example2:
marks = int(input('Enter your marks in maths: '))
if marks >=35:
            print('you got passing grades')
else:
            print('You have got failing grades')
            print('ThankYou, Study  Well next time')
                 
                 
if statement:
Lets have some example3:

marks = int(input('Enter the Marks: '))
if marks == 100:
     print('Perfect Score, Please tell your reading technic')
            
print('ThankYou')
     
multiway Selection:
     i. nested if
     ii.elif header

Since You know this Part, Giving basic flow  & Lets directly have some example:

if condition:
     action
else:
     if condition1:
          action1
     else:
          if condition2:
               action2
          else:
               -----------

Example4:
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

Example5:
#Example for nested if statement
grade = int(input('Enter Your Marks: '))
if grade >= 90:
            print('You got grade A')
else:
            if grade >= 80:
                 print('You got grade B')
            else:
                 if grade >= 70:
                      print('You have got grade B-')
                 else:
                      if grade >= 50:
                           print('you have got grade C')
                      else:
                           print('You got failing grade, Why You have not studied: ')
Example5:
#Example for elif

grade = int(input('Enter Your Marks: '))
if grade >= 90:
     print('You got grade B')
elif grade >= 80:
     print('You got grade B')
elif grade >= 70:
     print('You have got grade B-')
elif grade >= 50:
     print('you have got grade C')
else:
     print('You got failing grade, Why You have not studied, what is the problem: ')

Please practice all the if else examples which I have provided you in the earlier days for
good exposure.
     
     
    
