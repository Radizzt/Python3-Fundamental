#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    foo(2);
    foo(3);
    foo(4);
    foo();

#assigning a parameter makes it default
def foo(a=8):
    for i in range(a, 10):
        print(i, end=' ');
    print();
    
    
if __name__ == "__main__": main(); #let you call function after their call
