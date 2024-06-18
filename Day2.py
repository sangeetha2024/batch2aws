# CONTROL FLOW, LOOPS

"""
Conditionals: Boolean values and operators, conditional (if), alternative (if-else), chained
conditional (if-elif-else); Iteration: while, for, break, continue."""


"""
Conditional (if):
The if statement contains a logical expression using which data is compared and a decision
is made based on the result of the comparison.
Syntax:
if expression:
 statement(s)
If the boolean expression evaluates to TRUE, then the block of statement(s) inside the if
statement is executed. If boolean expression evaluates to FALSE, then the first set of
code after the end of the if statement(s) is executed.
"""

a = 3
if a > 2:
 print(a, "is greater")
print("done")
a = -1
if a < 0:
 print(a, "a is smaller")
print("Finish")


a=10
if a>9:
 print("A is Greater than 9")


a=10
b=20
if a>b:
 print("A is Greater than B")
else:
 print("B is Greater than A")
 
 
 a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('enter the number'))
if a>b:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
    
var = 100
if var == 200:
 print("1 - Got a true expression value")
 print(var)
elif var == 150:
 print("2 - Got a true expression value")
 print(var)
elif var == 100:
 print("3 - Got a true expression value")
 print(var)
else:
 print("4 - Got a false expression value")
 print(var)
print("Good bye!")




"""

In Python Iteration (Loops) statements are of three types:
1. While Loop
2. For Loop
3. Nested For Loops
While loop:
 Loops are either infinite or conditional. Python while loop keeps reiterating a block of
code defined inside it until the desired condition is met.
 The while loop contains a boolean expression and the code inside the loop is
repeatedly executed as long as the boolean expression is true.
 The statements that are executed inside while can be a single line of code or a block of
multiple statements.
Syntax:
 while(expression):
Statement(s)"""
i=1
while i<=6:
 print("Mrcet college")
 i=i+1
 
i=1
while i<=3:
 print("MRCET",end=" ")
j=1
while j<=1:
 print("CSE DEPT",end="")
 j=j+1
 i=i+1
 print()
i = 1
while (i < 10):
 print (i)
 i = i+1
"""
For loop:
Python for loop is used for repeated execution of a group of statements for the desired
number of times. It iterates over the items of lists, tuples, strings, the dictionaries and other
iterable objects"""
numbers = [1, 2, 4, 6, 11, 20]
seq=0
for val in numbers:
 seq=val*val
 print(seq)
 
#list of items
list = ['M','R','C','E','T']
i = 1
#Iterating over the list
for item in list:
 print ('college ',i,' is ',item)
 i = i+1
 
 
for i in range(1,6):
    for j in range(0,i):
        print(i, end=" ")
    print('')
