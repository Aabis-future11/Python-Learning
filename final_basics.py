# Write a program to print Twinkle twinkle little star poem in python.
print('''twinkle twinkle little star...
      how i wonder what you are,
      up above the world so high,
      like a diamond in the sky..
      ''')
#Use REPL and print the table of 5 using it.
# Install an external module and use it to perform an operation of your interest.
'''import pygame
import random

# Setup
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 150, 0)

font = pygame.font.SysFont("Arial", 24)

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (WIDTH, y))

def random_food(snake):
    while True:
        pos = (random.randint(0, WIDTH // CELL - 1) * CELL,
               random.randint(0, HEIGHT // CELL - 1) * CELL)
        if pos not in snake:
            return pos

def game():
    snake = [(300, 300), (280, 300), (260, 300)]
    direction = (CELL, 0)
    food = random_food(snake)
    score = 0
    running = True

    while running:
        clock.tick(10)  # speed — increase to make faster
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)

        # Move
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wall collision
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            break

        # Self collision
        if head in snake:
            break

        snake.insert(0, head)

        if head == food:
            score += 1
            food = random_food(snake)
        else:
            snake.pop()

        # Draw food
        pygame.draw.rect(screen, RED, (*food, CELL, CELL))

        # Draw snake
        for i, seg in enumerate(snake):
            color = GREEN if i != 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (*seg, CELL, CELL))
            pygame.draw.rect(screen, BLACK, (*seg, CELL, CELL), 1)

        # Score
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
        pygame.display.flip()

    # Game over screen
    screen.fill(BLACK)
    screen.blit(font.render(f"Game Over! Score: {score}", True, WHITE), (WIDTH//2 - 120, HEIGHT//2 - 20))
    screen.blit(font.render("Press R to restart or Q to quit", True, WHITE), (WIDTH//2 - 160, HEIGHT//2 + 20))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

game()'''
# Write a python program to print the contents of a directory using the os module.Search online for the function which does that.

# Label the program written in problem 4 with comments.
#-------------------------------------------------------------------------------#
#Write a python program to add two numbers. 
'''num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
print(f"the sum is {num1+num2}")'''
#Write a python program to find remainder when a number is divided by z. 
'''num=int(input("Enter the number:"))
z=int(input("enter divisor:"))
remainder=num%z
print(remainder)'''
#Check the type of variable assigned using input () function. 
'''a=input("enter1:")
b=input("enter2:")
c=input("enter3:")
print(int(float(a)))
print(float(b))
print(bool(int(c)))'''
#Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80 
'''a=34
b=80
print(a>b)'''

#Write a python program to find an average of two numbers entered by the user.
'''a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
avg=(a+b)/2 
print(avg)'''
#Write a python program to calculate the square of a number entered by the user.
'''a=int(input("Enter number:"))
print(a*a) '''
# 1.Write a python program to display a user entered name followed by Good Afternoon using input () function. 
'''name=input("Enter Your Name:")
str="GOOD AFTERNOON,        "
a=str.replace("      ",name)
print(a)'''

#2. Write a program to fill in a letter template given below with name and date. 
'''letter = "Dear <|Name|>,\nYou are selected!\n<|Date|> "
print(letter.replace("<|Name|>","Aabgeen").replace("<|Date|>","22th February"))
print()'''
#3. Write a program to detect double space in a string. 
'''str=input("Enter Data:")
print(str.find("  "))
#4. Replace the double space from problem 3 with single spaces. 
print(str.replace("  "," "))'''
#5. Write a program to format the following letter using escape sequence characters. 
'''letter = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter)'''
#1.Write a program to store seven fruits in a list entered by the user. 
'''a=[]
f1=input("enter fruit1:")
f2=input("enter fruit2:")
f3=input("enter fruit3:")
f4=input("enter fruit4:")
f5=input("enter fruit5:")
f6=input("enter fruit6:")
a.extend([f1,f2,f3,f4,f5,f6])
print(a)'''
#2.Write a program to accept marks of 6 students and display them in a sorted manner.
'''a=[]
m1=int(input("marks of s1:"))  
m2=int(input("marks of s2:"))  
m3=int(input("marks of s3:"))  
m4=int(input("marks of s4:"))  
m5=int(input("marks of s5:"))  
m6=int(input("marks of s6:"))  
a.extend([m1,m2,m3,m4,m5,m6])
a.sort()
print(a)'''
#3. Check that a tuple type cannot be changed in python. 
'''t=(12,23,34,45,56)
t[2]=56#>>gives error'''
#4. Write a program to sum a list with 4 numbers. 
'''list_numbers=[23,34,45,56]
sum=0
for i in list_numbers:
    sum+=i
print(sum)'''
#5. Write a program to count the number of zeros in the following tuple: 
'''a = (7, 0, 8, 0, 0, 9)
print(sum(a))'''
#1. Write a program to create a dictionary of Hindi words with values as their English 
#,translation. Provide user with an option to look it up! 
'''trans={"jaana":"going","bhagna":"running","tairna":"swimming","sona":"sleeping","khelna":"playing"}
word=input("enter hindi version:")
print(trans[word])'''


#2. Write a program to input eight numbers from the user and display all the unique 
#,numbers (once). 
'''s=set()
n1=int(input("enter number1:"))
n2=int(input("enter number2:"))
n3=int(input("enter number3:"))
n4=int(input("enter number4:"))
n5=int(input("enter number5:"))
n6=int(input("enter number6:"))
n7=int(input("enter number7:"))
n8=int(input("enter number8:"))
s.add(n1)
s.add(n2)
s.add(n3)
s.add(n4)
s.add(n5)
s.add(n6)
s.add(n7)
s.add(n8)
print(s)'''
#3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
'''s=set()
s.add('18')
s.add(18)
print(s)'''#yes we can 
#4. What will be the length of following set s2: 
'''s2 = set() 
s2.add(20) 
s2.add(20.0) 
s2.add('20') # length of s after these operations? ANS:-2
print(len(s2))'''
#5. s = {} 
#,What is the type of 's'? 
'''s={}
print(type(s))'''
#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
#,value and use key as their names. Assume that the names are unique. 
'''dict={}
n1=input("enter name:")
l1=input("enter language:")
n2=input("enter name:")
l2=input("enter language:")
n3=input("enter name:")
l3=input("enter language:")
n4=input("enter name:")
l4=input("enter language:")
dict.update({n1:l1,n2:l2,n3:l3,n4:l4})
print(dict)'''
#7. If the names of 2 friends are same; what will happen to the program in problem 
#,6? 
#Ans:-If names of two students are same it will take key value pair of the duplicate name entered first
#8. If languages of two friends are same; what will happen to the program in problem 
#it will be executed smoothly
#9. Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}
'''s={8,7,12,"Harry",[1,2]}'''
#no we cannot as elements of set cannot accept changeable(unhashable)elements
#A set can only take hashable(chnageable objects)..so when we print above set it will remove list
'''print(s)'''#it gives error
##1. Write a program to find the greatest of four numbers entered by the user. 
'''n1 = int(input("enter num1: "))
n2 = int(input("enter num2: "))
n3 = int(input("enter num3: "))
n4 = int(input("enter num4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("n1 is greatest")

elif n2 > n1 and n2 > n3 and n2 > n4:
    print("n2 is greatest")

elif n3 > n1 and n3 > n2 and n3 > n4:
    print("n3 is greatest")

else:
    print("n4 is greatest")'''
   
#2. Write a program to find out whether a student has passed or failed if it requires a 
#,total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#,take marks as an input from the user. 
'''maths=int(input("Enter marks obtained:"))
physics=int(input("Enter marks obtained:"))
chemistry=int(input("Enter marks obtained:"))
total_per=((maths+physics+chemistry)*100)/3
if total_per>=40 and maths>=33 and physics>=33 and chemistry>=33:
    print("Passed")
else:
    print("failed")'''
    
##3. A spam comment is defined as a text containing following keywords: 
#,“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
#,to detect these spams. 
'''data=input("enter data:")
if "Make a lot of money" in data:
    print("Spam detected")
elif "buy now" in data:
    print("Spam detected")
elif "subscribe this" in data:
    print("Spam detected")
elif "click this" in data:
    print("Spam detected")
else:
    print("No spam detected")'''

#4. Write a program to find whether a given username contains less than 10 
#,characters or not. 
'''username=input("Enter Username:")
if len(username)<10:
    print("Yes it contains less than 10 characters")
else:
    print("no it does not contain more than 10 characters")'''
##5. Write a program which finds out whether a given name is present in a list or not. 
'''list=["aabi","nani","sora","baba","jawan","tennet","sahibealam"]
name=input("enter name:")
if name in list:
    print("yes it exists")
else:
    print("it does not exist")'''
##6. Write a program to calculate the grade of a student from his marks from the 
#,following scheme: 
#90 – 100 => A+
#80 – 90 => A 
#70 – 80 => B 
#60 – 70  =>C 
#50 – 60 => D 
#<50 => F 
'''marks=int(input("Enter marks obtained:"))
if marks>90 and marks<=100:
    print("A+")
elif marks>80 and marks<=90:
    print('A')
elif marks>70 and marks<=80:
    print('B')
elif marks>60 and marks<=70:
    print('C')
elif marks>50 and marks<=60:
    print('D')
else:
    print('E')'''

##7. Write a program to find out whether a given post is talking about “Harry” or not.
'''post=input("enter post:")
if "Harry".lower() in post.lower():
    print("Yes it is talking about Harry")
else:
    print("No it is not talking about Harry")'''
##1. Write a program to print multiplication table of a given number using for loop. 
'''n = int (input("Enter number:"))
for i in range(1,11,1):
    print(f"{n}*{i}={n*i}")'''
##2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 
'''l = ["Harry", "Soham", "Sachin", "Rahul"] 
for i in l:
    if i=="Soham" or i=="Sachin":
        print(f"hi, {i}")'''

##3. Attempt problem 1 using while loop. 
'''n=int(input("Enter number:"))
i=1
while i <=10:
    print(f"{n}*{i}={n*i}")
    i+=1'''
##4. Write a program to find whether a given number is prime or not. 
'''n = int(input("enter number:"))

if n == 0 or n == 1:
    print("not a prime number")

else:
    is_prime = 1

    for i in range(2, (n//2) + 1):
        if n % i == 0:
            is_prime = 0
            break

    if is_prime == 0:
        print("number is not prime")
    else:
        print("number is prime")'''
##5. Write a program to find the sum of first n natural numbers using while loop. 
'''n=int(input("Enter Number:"))
sum=0
for i in range (0,n+1,1):
    sum+=i
print(sum)'''
##6. Write a program to calculate the factorial of a given number using for loop. 
'''n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1,1):
    fact*=i
print(fact)'''

##7. Write a program to print the following star pattern. 
'''  * 
    *** 
   ***** '''
'''n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print()'''


##8. Write a program to print the following star pattern: 
'''* 
  ** 
 *** ''' 
'''n=int(input("Enter no . of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()  '''
##9. Write a program to print the following star pattern. 
'''* * * 
   *   *   for n = 3 
   * * *'''  
'''n=int(input("Enter number of rows:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

##10. Write a program to print multiplication table of n using for loops in reversed order.
'''n=int(input("Enter number:"))
for i in range(10,0,-1):
    print(f"{n}*{i}={n*i}")'''
#---------------FUNCTIONS AND RECURSIONS----------------------#
'''
def greet():
    NAME=input("Enter Name:")
    print(f"GOOD DAY,{NAME}")
greet()'''
#1. Write a program using functions to find greatest of three numbers. 
'''def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greatest")
    elif b>a and b>c:
        print(f"{b} is the greatest")
    else:
        print(f"{c} is th greatest")
a=int(input("Enter number 1st:"))
b=int(input("Enter number 2nd:"))
c=int(input("Enter number 3rd:"))
greatest(a,b,c)'''

    
    
#2. Write a python program using function to convert Celsius to Fahrenheit. 
'''def cel_to_fahr(n):
    fahrenheit=((9/5)*n)+32
    print(f"{fahrenheit} is converted temperature in fahrenheit")
n=int(input("Enter temperature in degree celsius:"))
cel_to_fahr(n)'''

#3. How do you prevent a python print() function to print a new line at the end. 
'''def new_line(data):
    return f"{data}\n"
data=input("Enter the data:")
print(new_line(data))'''

#4. Write a recursive function to calculate the sum of first n natural numbers. 
'''def sum_natural(n):
    if n==0:
        return 0
    return n + sum_natural(n-1)
n=int(input("Enter Number:"))
print(f"{sum_natural(n)} is the sum of natural numbers uptill given number")'''

#5. Write a python function to print first n lines of the following pattern: 
'''*** 
    **               
     * - for n = 3 '''
'''def n_lines(n):
    for i in range (1,n+1):
        for j in range (0,i-1):
            print(" ",end="")
        for k in range (n,i-1,-1):
            print("*",end="")
        print()
n=int(input("no of lines:"))
n_lines(n)'''

#6. Write a python function which converts inches to cms. 
'''def inch_cm(n):
    return n*2.54
n=int(input("Enter inches:"))
print(f"{n}={inch_cm(n)} centimeters")'''
#7. Write a python function to remove a given word from a list ad strip it at the same time.
'''def strip(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n


l=["Harry","Sadrul","Shogul","ul","Rahul"]

print(strip(l,word="ul"))'''
#8. Write a python function to print multiplication table of a given number.
'''def table(n):
    for i in range(1,n+1):
        print(f"{n}*{i}={n*i}")
n=int(input("Enter a number:"))
table(n)'''
#--------FILE HANDLING--------------------#
#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 
'''with open("poems.txt","r") as file:
    content=file.read()
if ("Twinkle" in content):
    print("Yes,Twinkle word exists")
else:
    print("No Twinkle Word does not exist")
print(content)'''

#2. The game() function in a program lets a user play a game and returns the score 
##as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
##contains the previous Hi-score. You need to write a program to update the Hi
##score whenever the game() function breaks the Hi-score. 
'''import random
def game():
    score=random.randint(1,100)
    with open("highscore.txt","r") as f:
        highscore=f.read()
        if (highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0   
    print(f"Your score is {score}")
    if (score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    
game()'''
    
#3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
##different files. Place these files in a folder for a 13 – year old.
'''def tables(n):
    with open(f"Table_{n}.txt","w") as file:
        for i in range(1,11):
            file.write(f"{n}*{i}={n*i}\n")
        
for i in range(2,21):
    tables(i)'''


#4. A file contains a word “Donkey” multiple times. You need to write a program 
##which replace this word with ##### by updating the same file.
'''with open("donkey_file.txt","r") as f:
    content=f.read()
content=content.replace("Donkey","####")

with open("donkey_file.txt","w") as file:
    file.write(content)'''


#5. Repeat program 4 for a list of such words to be censored. 
'''list=['MAN','SHOPKEEPER','STRANGE','DOG','WOMAN','RED','CROWD']
for i in list:
    with open("censor.txt","r") as f:
        content=f.read()
        content=content.replace(i,"####")
    with open("censor.txt","w") as file:
        file.write(content)'''
#6. Write a program to mine a log file and find out whether it contains ‘python’.
'''with open("log.html","r")as file:
    content=file.readlines()
    lineno=1
for i in content:#else will only run when all for loop gets complete
    if "python" in i:
        print(f"Yes file contains python,Lineno:{lineno}")
        break
    lineno+=1
    
else:
         print("No it does not contain python")'''
#7. Write a program to find out the line number where python is present from ques 6. 
#8. Write a program to make a copy of a text file “this. txt” 
'''with open("this.txt","r") as file:
     content=file.read()
with open("copy.txt","w") as f:
     f.write(content)'''
#9. Write a program to find out whether a file is identical & matches the content of 
##another file. 
'''with open("copy.txt") as file:
    content=file.read()
with open("this.txt") as f:
    content2=f.read()
if content==content2:
    print("Files are same")
else:
    print("Files are not same")'''
#10. Write a program to wipe out the content of a file using python.
'''with open ("copy.txt","w") as file:
    file.write("")
    print("file deleted")'''

#11. Write a python program to rename a file to “renamed_by_ python.txt.
'''import os

if os.path.exists("copy.txt"):
    os.rename("copy.txt", "go.txt")
else:
    print("File does not exist)'''
#---------------OOPS---------#
'''class Employee:
    name="AABGEEN"
    age=12
    salary=140000
info=Employee()
print(info.name)
print(info.age)
Employee.salary=160000
Employee.role="Manager"
Employee.company="Glean"
print(f"{info.salary}\n{Employee.role}\n{info.company}")
rohan=Employee()
rohan.name="Rohan Ronit"
Employee.company="Bain"
rohan.tenure=10
rohan.role="Project Manager"
print(f"{rohan.name}\n{rohan.age}\n{rohan.salary}\n{rohan.tenure}\n{rohan.role}\n{rohan.company}")'''

#Here tenure and role are object attributes and name,age and salary are class attributes
##as they directly belong to class
'''class Employee:
    language="Python"
    salary=1500000
    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
harry=Employee()
harry.getinfo()
Employee.getinfo(harry)'''
#1. Create a class “Programmer” for storing information of few programmers 
##working at Microsoft. 
'''class Programmer:
    def __init__(self,name,language,experience):
        self.name=name
        self.language=language
        self.experience=experience
    def show(self):
        print(f''The name of programmer is {self.name},language known is {self.language} and experience owned is {self.experience}'')
prog1=Programmer("Harry","Python",20)
prog2=Programmer("aabi","Javascript",25)
prog1.show()
prog2.show()'''
#2. Write a class “Calculator” capable of finding square, cube and square root of a number. 
'''import math
class calculator:
    def __init__(self,number):
        self.number=number
    def show(self):
        print(f"the square is {(self.number)*(self.number)}")
        print(f"the cube is {(self.number)*(self.number)*(self.number)}")
        print(f"the square root is {math.sqrt(self.number)}")
number=calculator(81)
number.show()'''
#3. Create a class with a class attribute a; create an object from it and set ‘a’ 
##directly using ‘object.a = 0’. Does this change the class attribute? 
'''class new:
    a=23
    def show():
        print("new age")
object=new()
print(object.a)#prints class attribute as no instance attribute was present before
new.a=0 # instance attribute is set now
print(f"the value of a is {new.a}")'''#yes object attribute overwrites the class attribute
#4. Add a static method in problem 2, to greet the user with hello. 
'''import math
class calculator:
    def __init__(self,number):
        self.number=number
    @staticmethod
    def greet():
        print("Hello User")
    def show(self):
        print(f"the square is {(self.number)*(self.number)}")
        print(f"the cube is {(self.number)*(self.number)*(self.number)}")
        print(f"the square root is {math.sqrt(self.number)}")
number=calculator(81)
number.greet()
number.show()'''
#5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
##and get fare information of train running under Indian Railways. 
'''class Train:
    def __init__(self,number,time,duration,fare):
        self.number=number
        self.time=time
        self.duration=duration
        self.fare=fare


    def book(self):
      print(f"The train number{self.number} is booked at {self.time} and duration is {self.duration}")
    def get_status(self):
        print(f"The train number {self.number} is On Time")
    
    def get_fare(self):
        print(f"The train number {self.number} fare is {self.fare}")
        
    def showdetails(self):
        print(f"The Train number is {self.number}\n,the time is {self.time}\n,the duration is {self.duration}\n,the status is on time\nand fare is {self.fare}\n")
Shatabdi=Train(2345,"17:00","5 hrs",1500)
Shatabdi.book()
Shatabdi.get_status()
Shatabdi.get_fare()
Shatabdi.showdetails()'''
#6. Can you change the self-parameter inside a class to something else 
##(say “harry”). Try changing self to “slf” or “harry” and see the effects.
'''class student:
    def __init__(harry,name,rollno,section,grade):
        harry.name=name
        harry.rollno=rollno
        harry.section=section
        harry.grade=grade
    def showinfo(slf):
        print(f"The name of student is {slf.name}, the roll no. is {slf.rollno} and grade is {slf.grade}")
st1=student('AABGEEN',43,'G1\'H\'','A')
st1.showinfo()'''#NO NOTHING WILL HAPPEN AS IT IS JUST A VARIABLE WHICH IS REFERENCE TO THE OBJECT CREATED..
#AND EVERYTIME WE CHANGE PARAMETER NAME ONLY THE NAME OF VARIABLE THAT REFERENCES IT INSIDE METHOD CHANGES
#BUT THE OBJECT REMAINS SAME

