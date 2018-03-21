
'''_________________________________ Class ______________________________________ '''
''' ######### create a new class ###################'''
class Employee:
    'Common base class for all employees, it is the first comment line below Class '

    empCount = 0 # it is class attribute, Employee.empCount, also it is object attribute, emp1.empCount '
    __secretCount = 0  # same function with empCount, but you can use emp1.__secreteCount to check the value, it is invisible

    def __init__(self, name, salary):  # __int__ is a special method, initialization method '''
        self.name = name  # ''' self is an object, name is the object attribute, not class attribute, emp1.name '''
        self.salary = salary  # ''' emp1.salary '''
        Employee.empCount += 1
        self.__secretCount += 1

    def displayCount(self): # ''' object method, emp1.displayCount() '''
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self): # ''' object method, emp1.displayEmployee() '''
        print "Name : ", self.name,  ", Salary: ", self.salary

    def __add__(self, other):   # write the object operator
        return self.salary + other.salary



'''##################### create objects ######################### '''

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.name
emp1.salary
emp1.empCount
emp1.__secretCount    # __secretCount is invisible attribute
emp1._Employee__secretCount   # it is how to check the invisible attribute
emp1.displayCount()
emp1.displayEmployee()
emp1 + emp2

'''###################### add/remove/modify attributes of class/object ################ '''
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
delattr(empl, 'age')    # Delete attribute 'age'

'''############################ build-in Class Attribute ##################### '''

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
'''Module name in which the class is defined. This attribute is "__main__" in interactive mode.'''
print "Employee.__bases__:", Employee.__bases__
''' A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.'''
print "Employee.__dict__:", Employee.__dict__
'''Dictionary containing the class's namespace.'''

'''############################### Class Inheritance ############################# '''

class Parent:        # define parent class
   parentAttr = 100

   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr
       # we use Parent here, because we want to chang the Class Parent attribute,
       # when you use self.parentAttr, u just change the object attribute

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

   def sameMethod(self):
       print 'Calling parent method'


class Child(Parent): # define child class, end inheritance from parent class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def sameMethod(self):      # use the same method name to parent method, it is overriding
       print 'Calling child method'



c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.parentAttr
c.getAttr()          # again call parent's method
c.sameMethod()

'''##################### check the relationship between parent and subclass ############ '''
issubclass(Parent, Child)     # False
issubclass(Child, Parent)     # True
isinstance(c, Child)          # if c is the object/instance of class Child








