#empty set is a  dictionary
#sets are unordered and have no index values for accessing elements
#prints the same integer
#randomn values in set are saved in memory using hash
#hashing of numbers may show number itself for small numbers
# for loop iterates on a new sorted list when we use sorted(set_name)
#>this is the reason why it returns ordered values 
#keys are index for accessing values in a dictionary

#EXCEPTION HANDLING:
'''marks=int(input("enter marks:"))
try:
    if marks>100 or marks<0:
       raise ValueError("your marks must be between 0 to 100")
    else:
       print("your result is evaluated")
except Exception as error:
   print(f"there is an error due to {error}")
finally:
   print("no matter what is happening")
print("completed")

r=open('nani.py',"x")
r.write("Lets start something new")# W IS KNOWN FOR OVERWRITING.
#OOPS IS PYTHON:
#CLASSES:
class animal:
    species="dog"#attribute
    def make_sound(self):
        print("bark!")  #method
print(animal().species)
animal().make_sound()

#Objects:
class student:
    def __init__(self,name):
        self.name=name
s=student("riya")
print(s.name)
class bag:
    def __init__(self,material,pockets,zip):
        print(self)
        self.material=material
        self.pockets=pockets
        self.zip=zip
    def show(self):
        print(f"your object details are:{self.material},{self.pockets}and{self.zip}")
reebok=bag("nylon",5,6)
safari=bag("silk",4,2)

reebok.show()
safari.show()
class demo:
    def __init__(self):
        self.name="aabi"   #public
        self._age=34       #protected
        self.__height="5'9"#private
    def __show(self):
        print("inside class:")
        print("public:",self.name)
        print("protected:",self._age)
        print("private:",self.__height)
#since these instance attributes are present inside class so we can access them
# accessing themis only possible when there are no double underscores before show      
obj=demo()
obj.__show()#it will tell demo object has no attribute show'''


class demo:
    def __init__(self):
        self.name="aabi"   #public
        self._age=34       #protected
        self.__height="5'9"#private
    def show(self):
        print("inside class:")
        print("public:",self.name)
        print("protected:",self._age)
        print("private:",self.__height)
#since these instance attributes are present inside class so we can access them
# accessing themis only possible when there are no double underscores before show      
obj=demo()
obj.show()#it will print all the methods and objects





        

    

        



       


















