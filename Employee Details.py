class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
class Employed(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)

a=Employed('raaj',5782319,130000,'teacher')

a.display()