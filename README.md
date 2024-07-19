1.Python Program to Generate a Random Number
import random
print(random.randint(0,9))

2.Python Program to Convert Kilometers to Miles
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

3.Python Program to Convert Celsius To Fahrenheit

celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

4.Python Program to Check if a Number is Positive, Negative or 0
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

5.Python Program to Check if a Number is Odd or Even

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

6.Python Program to Check Leap Year

year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

7.Python Program to Find the Largest Among Three Numbers
 
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

8.Python Program to Check Prime Number

num = 29
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
  
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

9.Python Program to Print all Prime Numbers in an Interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

10. Python Program to Find the Factorial of a Number

num = 7

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

