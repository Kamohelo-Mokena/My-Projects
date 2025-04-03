#1
print("Hello World!") 
    

#2
age = 10 
print(age) 

#3
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
addition = num1 + num2
print(addition) 

#4
name = input("enter your name:") 
print("Greetings ", name) 

#5
fruits = ["apple", "banana", "pineapple", "date", "lemon"] 
for i in fruits:
    print(i) 
    
    
#6
num = int(input("enter a number:")) 
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative") 
elif num == 0:
    print("the number is 0") 
    
    
#7
for i in range(1,11): 
    print(i) 
    
    
#8
launch = 10
while launch > 0:
    print(launch) 
    launch -=1

    
#9
def product(num_1,num_2):
    return num_1 * num_2 
    multiplication = num_1 * num_2 
    print(multiplication) 
num_1 = int(input("enter a number: ")) 
num_2 = int(input("enter a number: "))
print(num_1 * num_2) 
product(num_1, num_2)  

    
#10
token = "a dozen kittens"
token1 = token.upper() 
print(token1) 

    
#recap 2 

#create a dictionary with three key value pairs and print one of the values
__dict__ = {'ned':2, 'tod':3, 'ben':6} 
print(__dict__['tod']) 
    

#use a list comprehension to create a list of squares from 1 to 10
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in squares:
    print(i **2) 
    
    
#write a program that handles division by zero using try, except, block
def division(number, number2): 
    try:
        result = number / number2
    except ZeroDivisionError: 
        return "cannot divide by zero" 
    else:
        return result 
    
number = int(input("enter a number: ")) 
number2 = int(input("enter a number: ")) 
result = division(number, number2)  
print(result) 
    
    
#file i/o
#write a program that reads a textfile and prints its contents 

file = open("my_second_file.txt", "w") 
file.write("Neo ")
file.close() 

file = open("my_second_file.txt", "a")
file.write("Moteetee ") 
file.write("\nhello everyone")
file.write("\ni am a student at gca") 
file.close() 

with open("my_second_file.txt", "r") as file: 
    content = file.read() 
    print(content) 
        

#modules: import the math module and use it to calculate the square root of sixteen 

from math import *

number = 16
print(sqrt(number)) 
    
    
#lambda: write a lambda function that adds two numbers and call it 
add_numbers = lambda x, y: x + y 
  
result = add_numbers(10, 9) 
print(result) 
    
    
#sets: create two sets and print their union and intersection
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8} 

union_of_sets = set1.union(set2) 
print("union:", union_of_sets)

intersection_of_sets = set1.intersection(set2) 
print("intersectiion:", intersection_of_sets) 
    
    
#oop: creating a class: define a class called duck or dog, with attributes for name and age. 
#add a method to the dog class that adds a description to it.
#create a class cat that inherits from dog class

class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        
    def bark(self):
        return f"{self.name}, says Woof!"
    
my_dog = Dog("Buddy", 3) 
print("My dog's name is ", my_dog.name, "and it is ", my_dog.age, "years old.") 
print(my_dog.bark()) 

class Cat(Dog): 
    def meow(self): 
        return f"{self.name} says Meow!"
    
my_cat = Cat("Whiskers", 2)
print(my_cat.meow()) 
print(my_cat.bark()) 

class Duck: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
my_duck = Duck("Daffy", 5) 
print("My duck's name is ", my_duck.name, "and it is ", my_duck.age, "years old.") 