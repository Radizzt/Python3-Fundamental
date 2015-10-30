#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1, 2, 3, 5 ,6 ,7 ,8)

#list of optional arguments
def testfunc(n, n2, *args):
    #args is a tuple object
    print(type(args));
    print(n, n2, args);
    for n in args:
        print(n, end="\n");

if __name__ == "__main__": main()
