#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print("The duck can't bark");
    
    def fur(self):
        print("The duck has feather")

class Dog:
    def bark(self):
        print("woof");
    
    def fur(self):
        print("dog has brown/white fur");
        
    def quack(self):
        print('dog cannot quack!')

    def walk(self):
        print('Walks like a dog.')
        
def main():
    donald = Duck()
    fido = Dog();
    
    in_the_forest(donald);
    in_the_pond(fido);
    
def in_the_forest(dog):
    dog.bark();
    dog.fur();
    
def in_the_pond(duck):
    duck.quack();
    duck.walk();

#     for o in (donald, fido):
#         o.quack();
#         o.walk();
#         o.bark();
#         o.fur();

if __name__ == "__main__": main()
