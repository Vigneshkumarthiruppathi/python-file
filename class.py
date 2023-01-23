class person:
    def__init__(self,name,age)
    self.name = name
    self.age = age
   
    def__repr__(self):
        return f "person(name ='{self.name}',age'= {self.age}')"
        
    def__eq__(self,other):
        return self.name == other.name and self.age == other.age
