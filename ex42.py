## Animal is-a object

class Animal(object):
	pass

# Dog is-a Animal
class Dog(Animal):
	def __init__(self,name):
		self.name = name

# Cat is-a animal
class Cat(Animal):
	def __init__(self,name):
		self.name = name

# person is a object
class Person(object):
	def __init__(self,name):
		self.name = name  #person has-a name
		self.pet = None	  #person has-a pet

# Employee is-a person
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee,self).__init__(name)
		self.salary = salary  #Employee has-a salary

class Fish(object):
	pass
class Salmon(Fish):
	pass
class halibut(Fish):
	pass

rover = Dog("Rover")
satan = Cat("Satan")
mary  = Person("mary")

mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = halibut()

