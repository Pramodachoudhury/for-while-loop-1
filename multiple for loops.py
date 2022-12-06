#write a program that reads numbers from the user until a blank line is entered.
#your program should display the average of all of the values entered by the user.
#then the program should display all of the below average values,followed by all of the average values (if any),
#followed by all of the above average values. an appropriate label should be displayed before each list of values.
"""n=int(input('enter a number'))
l=list()
while n!=0:
    l.append(n)
    n=int(input('enter a number'))
print('the list of element enter by',l)
avg=sum(l)/len(l)
print('the average of element',avg)
for i in range(0,len(l)):
    if l[i]<avg:
        print('the element are below',l[i])
for i in range(0,len(l)):
    if l[i]==avg:
        print('the element are equal averaage',l[i])
for i in range(0,len(l)):
    if l[i]>avg:
        print('the element are above average',l[i])"""
#An integer, n, is said to be pedeer when the sama of the properties of an equal to a.
#For example. 28 is a perfect her became is proper des 12 4.7 and 14, and 1+2+4+7-14=28
#Write a function that determines whether or poste perfect. your function will take one parametr .
#if that parameter is a perfect number then your function will return True. Otherwise will will return False .
#In addition write a main program that uses your function to identify and display all of the perfect numbers between 1 and 10.000.
#Import your solution ?
"""n=int(input('enter a number:'))
l=list()
for i in range(1,n):
    if n%i==0:
        l.append(i)
print(l)
lsum=sum(l)
if lsum==n:
    print('its a perfect number')
else:
    print('its not a perfect number')"""

"""for i in range(1,10001):
    s=0
    n=i
    for  j in range(1,n):
        if i%j==0:
            s=s+j
    if s==i:
        print('its prefect',i)"""
#
"""s=str(input('enter a word:'))
l=list()
while s!=" ":
    l.append(s)
    s=str(input('enter a next word :'))
print(l)
a=len(l)
if a==1:
    print(l[0])
elif a==2:
    print(l[0],"and",l[1])
else:
    for i in range(a-2):
        print(l[0],end=",")
    for i in range(a-2,a-1):
        print(l[i],end="and")
    for i in range(a-1,a):
        print(l[i])"""

#in order to  win top prize in a particular lottery,one must match all 6 numbers on his and her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
#organizer.Write a program that generate a random selection of 6 numbers for a lottery ticket.Ensure that all 6 number selected do not contain any duplicates
#Display the numbers in ascending number?
import random
lott_number=list()
for i in range(1,6+1):
    number=random.randint(1,49)
    lott_number.append(number)
print(lott_number)
lott_number.sort()
print("print the lottery number are ascending order:",lott_number)
          














