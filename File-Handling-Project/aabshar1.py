class doing:
    name="aabi"
    def __init__(self,age,height):
        self.age=age
        self.height=height
    def show(self):
        print(self.age,self.height)
obj1=doing(11,"5'8")
print(obj1.name)
print(obj1.age)
print(obj1.height)
obj1.show()


