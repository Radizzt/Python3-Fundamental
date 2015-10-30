#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(6, 25, 3):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args);
    if numargs < 1: raise TypeError("Require atleast one Argument");
    elif numargs == 1:
        stop = args[0];
        start = 0;
        step = 1;
    elif numargs == 2:
        (start, stop) = args;
        step = 1;
    elif numargs == 3:
        (start, stop, step) = args;
    else:
        raise TypeError("Too may arguments, only can have at most 3 arguments");
    
    i = start;
    while i <= stop:
        yield i;#next time the function is call it starts after yield;
        i +=step;
if __name__ == "__main__": main()
