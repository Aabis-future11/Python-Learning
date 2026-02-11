#PART-1:PYTHON BASICS & LOGIC(till functions)
#QUESTION SET 1: Questions on conditional statements(if-else ; if-elif-else ;if)

#QUESTION SET 2: Questions on loops (for loop):-
#- Accept an integer and Print hello world n times
n=int(input("enter integer:"))
for i in range(n):
    print("hello world")
print()

#Print natural number up to n
n=int(input("enter number:"))
for i in range(1,n+1,1):
   print(i)
print()
#Reverse for loop. Print n to 1
n=int(input("enter integer:"))
for i in range (n,0,-1):
    print(i)
    print()

#Take a number as input and print its table
n=int(input("enter the number:"))
for i in range(1,11,1):
   print("",n,"*","",i,"=","",n*i)
print()

#Sum up to n terms
n=int(input("enter the number:"))
sum=0
for i in range(n):
    sum+=i
print(sum)
print()
#Factorial of a number
n=int(input("enter number:"))
fact=1
for i in range(1,n+1,1):
    fact*=i             
print("factorial=",fact)#[assignment statement is not allowed inside print() ;like print(fact*=i) not allowed , error!]
print()
#Print the sum of all even & odd numbers in a range separately
n=int(input("enter number:"))
sum_even=0
sum_odd=0
if  n>=0:
    for i in range(0,n+1,1) :
       if(i%2==0):
        sum_even+=i
       else:
        sum_odd+=i
    print("sum of even numbers=",sum_even)
    print("sum of odd numbers=",sum_odd)

else :
  print("not a valid number")
print()
 

# Print all the factors of a number(integers)
n=int(input("enter number:"))
if(n>0):
    for i in range(1,n+1,1):
        if(n%i==0):
         print("factor of",n,"is:",i)
else:
    print("no factor exists")
print()


#Accept a number and check if it a perfect number or not.A number whose sum of factors is equal to the number itself
n=int(input("enter the number:"))
sum=0
if n>=0:
    for i in range(1,n,1):
       if(n%i==0):
         sum+=i

    if(sum==n):
      print("number is a perfect number")
    else:
      print("number is not a perfect number")
else:
   print("not a valid number")
print()

#Check wether the number is prime or not
n=int(input("enter number:"))
is_prime=1
if n>1:
    for i in range(2,(n//2)+1,1):
        if(n%i==0):
           is_prime=0
        break
    if(is_prime==1):
      print(f"{n} is a prime number")
    else:
      print(f"{n} is not a prime number")
else:
    print("not a valid number")
print()

#Reverse a string without using in build functions
str1="AABGEEN AABSHAR"
str2=""
for i in range (14,-1,-1):
   str2=str2+str1[i]
print("reversed string=",str2)
print()
   

#Check string is Pallindrome or not
str1=input("enter the string:")
str2=""
for i in range(len(str1)-1,-1,-1):
   str2+=str1[i]

if(str1==str2):
   print("given string is palindrome")
else:
   print("given string is not a palindrome")
   print()

#Count all letters, digits, and special symbols from a given string.Given: str1 = "P@#yn26at^&i5ve" Expected Outcome:Total counts of chars, digits, and symbols.
a= "P@#yn26at^&i5ve"
chars=0
digits=0
symbols=0
for i in a:
   if i.isdigit():
      digits+=1
   elif i.isalpha():
      chars+=1
   else:
      symbols+=1
print(f"total characters are:{chars}\ntotal digits are:{digits}\ntotal symbols are:{symbols}")

#QUESTION SET 3: Questions on loops (while loop):-

#Separate each digit of a number and print it on the new line
n=int(input("enter number:"))
while n>0:
    a=n%10
    n=n//10
    print(a)
#Accept a number and print its reverse
n=int(input("enter a number:"))
rev=0
while n>0:
    a=n%10
    rev=(rev*10)+a
    n=n//10
    
print("reverse of number is:",rev)
print()

#Accept a number and check if it is a pallindromic number (If number and its reverse are equal?)
n=int(input("enter a number:"))
rev=0
temp=n
while n>0:
    a=n%10
    rev=(rev*10)+a
    n=n//10
    
print("reverse of number is:",rev)
if temp==rev:
    print(f"{temp} is a pallindromic number")
else:
    print(f"{temp} is not a pallindromic number")
print()

#Create a random number guessing game with python.
import random
secret_number = random.randint(1, 10) # This picks a number between 1 and 10
tries=0

while secret_number!=n:
    n=int(input("throw a number(1-10):"))
    tries+=1
    if n>10 or n<0:
       print("invalid number entered")
    elif(n==secret_number):
        print("match found")
        break
    print("no match found")
print("You got the right number")
print("no of tries=",tries)
#QUESTION SET 4: Questions on Functions:-

