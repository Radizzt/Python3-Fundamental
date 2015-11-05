#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk(self): print("i have something to say");
    def walk(self): print("hey Im walking");

#Duck inherit from Animal
class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk();#super function
        print('Walks like a duck.')
    
    def talk(self):
        print("duck talk");

class Goose(Duck):
    def laugh(self):
        print("laughing");
        
    def talk(self):
        super().talk();#only goes to the parent, not grandparent
        print("GOose talking!");
        
def main():
    donald = Duck()
    goose = Goose();
    print(donald);
    donald.quack()
    donald.walk()
    donald.talk();
    goose.laugh();
    goose.talk()
    goose.walk();

if __name__ == "__main__": main()
