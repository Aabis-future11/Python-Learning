import random
gamemap={
    -1:"Snake",
    0:"Water",
    1:"Gun"
}#Taking a dictionary for key and value pairs pointing to Snake Water and Gun
choice=int(input("Enter your Choice -1 for Snake/0 for Water/1 for Gun:"))#inputting choice in form of(-1/0/1) 
Computer=random.choice([-1,0,1])#using randomn module for intializing randomn values between(0,1,-1)
print(f"You chose {gamemap[choice]}")#specifying your's and Computer's Choice
print(f"Computer chose {gamemap[Computer]}")
#Writing conditions for Win and Lose
if choice==Computer:
    print("It's a Draw!!")
elif (choice==0 and Computer==1) or \
    (choice==1 and Computer==-1) or \
    (choice==-1 and Computer==0):
    print("You Win!")
else:
    print("You Lose!")