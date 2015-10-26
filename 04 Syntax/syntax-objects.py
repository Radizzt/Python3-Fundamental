#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#define class

class Egg:
    #instance member Variable
    test = "test";
    #constructor
    def __init__(self, kind = "fried"):
        self.kind = kind;
        
    def whatKind(self):
        return self.kind;

def main():
    scramble = Egg("scramble");
    
    print(scramble.whatKind() + " " + scramble.test);

if __name__ == "__main__": main(); #let you call function after their call
