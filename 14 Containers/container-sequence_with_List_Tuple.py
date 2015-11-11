#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #tuple is immutable
    tup = (1,2,3,4,5);
    tup2 = (1,); #1 tuple
    print(tup[2]);
    #tup[2] = 42; #does not work
    #list is mutable
    l = [1,2,3,4,5,6]
    print(l[3]);
    l[3] = 42;
    print(l[3])
    

if __name__ == "__main__": main()
