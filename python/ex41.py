##Animal is-a object
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name 
		self.name = name 

## Cat is-a animal 
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person 
class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
##Fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

##frank is-a employee
frank = Employee("Frank", 120000)

##frank has-a pet
frank.pet = rover

##flipper is-a fish
flipper = Fish()

##crouse is-a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()
