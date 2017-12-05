While loop:While loop is similar to an if statement. It executes the code inside of it if some
condition is true. The difference is that the while loop will continue to execute as long
as the condition is true.In Other words, Instead of executing if something is true, It executes
while that thing is true.

while condition:
     statements

#Example for while loop:

count = 1
while count <=5:
     print(count)
     count++
print('Bye Bye')

#Example2
num = 1

while num <= 10:
     print(num ** 2)
     num = num + 1

#Example3

choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
     choice = input('I didnot catch that. Enter again: ')

#Example 4: Infinte while loop blunders
count = 1
while count <=5:
     print(count)
     
print('Bye Bye')


While / else: Something completely different about the Python is the while/else construction.
While/else is similar to if/else. But there is a difference. The else block will execute
anytime the loop condition is evaluated to False. This means that it will execute
if the loop is never entered or if the loop exits normally. If the loop exits as the results
of a break. the else will not be executed.

In this example,  the loop will break if a 5 is generated and the else will not execute.
Otherwise after 3 numbers are generated. The loop will become false and the else
will execute.

#Example 5: 
import random

print('Luncky Numbers! 3 numbers will be generated. ')
print('If one of them is a 5, you lose! ')

count = 0

while count < 3:
     num = random.randint(1,6)
     print(num)
     if num == 5:
          print('Sorry, You lose')
          break
     count = count + 1

else:
     print('you win')
