'''dict={
    "aabi":13,
    12:34,
    34:"aabgeen"

}
#print(dict.items())
#print(dict.keys())
#print(dict.values())
#dict.update({"nani":34,12:"Imam"})
#print(dict)
#print(dict.get("nani"))#prints None
#print(dict["nani"])#prints Error
dict1={}#empty dictionary
s1={1,2,3}#set
s2=set()#this is used for preparing set
print(type(s2))
s3={2,4,4,5,6,7,3,9}
print(s3,type(s3))#sets don't print duplicate elements
s3.add(345)
print(s3,type(s3))
print(len(s3))
s3.remove(345)
print(s3)'''
'''with open("new.txt", "r+") as file:
    file.write("I am Good jake and lets become the mastermind of the planet")
    file.seek(0)   # Move pointer back to start
    content = file.read()

print(content)'''
'''class report:
    Name="Aasha"
    blood_group='A'
    age=12
    medicine="Erythromycin"
    condition='Headache'
    def greet(self):
        print(f"Hi,{self.Name}")  
    def showrep(self):
        print(f''Name of patient is {self.Name},age is {self.age},blood group is {self.blood_group},medicine prescribed is{self.medicine},condition is {self.condition}'')
nadeem=report()
nadeem.Name="Nadeem"
nadeem.age=34
report.blood_group='o+'
nadeem.greet()#report.greet(nadeem), it is taking one positional argument
nadeem.showrep()#report.showrep(nadeem).it is also taking one positional argument'''
'''class car:
    name="Bentley"
    colour="red"
    year=2026
    Engine="Yes,it is Diesel#No need to include this as you have used dunder method and constructor for creating memory of object
    def __init__(self,name,colour,year,Engine):#THIS IS A DUNDER METHOD AS IT RUNS AS SOON AS AN OBJECT IS CREATED
        print("We are specifying a car")
        self.name=name
        self.colour=colour
        self.year=year
        self.Engine=Engine
    @staticmethod#This does not require a self parameter
    def greet():
        print("Congratulations , Sir!!")
    def showdetails(self):
        print(f"The name of car is {self.name},the color is {self.colour},the year is {self.year} and engine is {self.Engine}")
Ronit=car("Buggati","Yellow",2030,"Yes, it is a petrol Engine")
Ronit.showdetails()
print(Ronit.name)
Aabgeen=car("Porsche","Blue",2025,"NO,it is an electric car")#As soon as an object is created the dunder method runs
Aabgeen.showdetails()
print(Aabgeen.name)
print(Aabgeen.name,Aabgeen.colour,Aabgeen.year,Aabgeen.Engine)'''
#single level inheritance:-
'''class Employee:
    name='RAHUL'
    company='ITC'
    def show1(self):
        print(f"The name of employee is {self.name} and company is {self.company}")
class Role(Employee):
    Position="Software Developer"
    Language="Python"
    def show2(self):
        print(f"THE POSITION OF {self.name} is {self.Position} and language known is {self.Language}")
e1=Employee()
e2=Role()
e2.show1()
e2.show2()#name and company along with function or method show1 has been inherited as parent class in child class Role'''
#Multilevel inheritance
'''class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
e1=Employee()
e2=Programmer()
e3=Manager()
print(e1.a)
print(e2.b,e2.a)
print(e3.a,e3.b,e3.c)'''



'''class Employee:
    a=1
    def __init__(self):
        print("Constructor of Employee")
class Programmer(Employee):
    b=2
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
class Manager(Programmer):
    c=3
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")

o1=Employee()#Dunder method executes as soon as object instantiation is created
o2=Programmer()
o3=Manager()
print(o1.a)
print(o2.a,o2.b)
print(o3.a,o3.b,o3.c)'''
#multiple inheritance
'''class father:
    height="5'8 inch"
    hair_texture="Black"
class mother:
    color_eyes="Blue"
    skin_colour="Fair"
    def __init__(self):
        print(f"The colour of eyes is {self.color_eyes} and skin colour is {self.skin_colour}")
class child(father,mother):
    def __init__(self):
        super().__init__()
        print(f''The child's height is {self.height},hair texture is {self.hair_texture},eye colour is {self.color_eyes} and skin colour is {self.skin_colour}'')
p1=mother()
print(p1.color_eyes)
c1=child()
print(c1.hair_texture)'''
#class method
'''class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")#if self was there and class method was removed then the value would have been 45
e1=employee()
e1.a=45
e1.show()'''
#static method
'''class math:
    @staticmethod
    def add(a,b):
        return a+b
print(math.add(12,13))'''
#property decorator
'''class Circle:
    def __init__(self, radius):
        self._radius = radius   # internal variable

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
c = Circle(5)
print(c.area) '''  # No parentheses
