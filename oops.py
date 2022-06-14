# Object oriented program vs Procedural oriented programming:
# OOP: In object oriented, the entire code is implemented using the concepts of classes and Objects
# POP: In procedure oriented, the entire code is implemented using the concepts of functions
# ====================
# Where do we use OOPS and POP?
# OOP is used for core python programmming, web development.
# POP is used for python scripts and Data Science etc
# What is a class? A group of some similar items, for example, group of students who have similar objectives
# In the programming, a class is a blue print that is containing group of functions in a similar memory location.
# Implementing group of  functions in a class in a single memory location, so that we can call the functions.
# Class is a logial entity that contains attributes and methods.
# attributes: are the variables that belong to a class. 
# methods: Fnctions inside a class.
# Attributes outside class are referred as variables. Methods outside a class are called functions.
# Objects: Instace of a class, a real world entity that will be having certain behaviour, identity and state.
# state --> represented by a attribute of a object
# Behaviuor --> represented by a method of an object
# Identity --> Unique name to an object
# Example: Dogs --> Class
# Dog1, Dog2 : Objects of the class Dog
# Class Dog: Breed, Color, Age, Gender (attributes), eat(), bark(), sleep() (methods)
# Features of dog can be represented by attributes; Breed, Color, Age, Gender (attributes)
# Behaviour of dog can be represented by method. eat(), bark(), sleep() (methods)
# Name of dog is identity
# Dog1 = Max --> breed = lab, color = Golden, age = 2, gender = Male
# Dog2 = Daisy ; --> breed = pomarian, color = White, age = 1, gender = Female
#Syntax to create a class: 
# class classname():
       # statements
# Syntax to create an object: object_name = classname()
# self: the first parameter inside a method definition
# self represents instance of a class 
# With self we can access the attributes and methods of the class.
# Self acts as a reference for the other attributes in the class.
# We don't have to initialize or assign a value to the self
# Constructors are used instantiating an object,
# to initialize(assign the values) to the data members of the class when an object is created.
# In python __init__() method is called as a contructor
# It will called automatically whenever an object is created.
class Dogs:
    def __init__(self,breed,color,age,gender):
        self.breed=breed
        self.color=color
        self.age=age
        self.gender=gender
    def eat(self):
        print(self.breed)
        print("The dog is eating")
    def sleep(self):
        print(self.color)
        print("The dog is sleeping")
    def bark(self):
        print(self.gender)
        print("The dog is barking")
max=Dogs('lab','white',1,'Male')
Daisy=Dogs('Pom','Black','2','Female')
max.eat()
Daisy.sleep()