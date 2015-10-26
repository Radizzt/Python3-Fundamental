#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#assignment
def main():
    a = 1;
    b, c = 2, 3;
    d = (1, 2,3,4,5); #tuple
    e = [1,2,3,4,5];
    
    
    print(a, b, c);
    print (type(a), a);
    print(d);
    print(e);
    print("This is the syntax.py file.")
    print("a: {}, b: {}, c: {}".format(a, b ,c));
    
if __name__ == "__main__": main(); #let you call function after their call
