#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print(True and False);
    print(True and True);
    print(True or False);
    print(False or False);
    
    a,b = 0,1;
    x,y="zero","one";

    print(x<y);
    print(a<b);
    print("yes") if a<b and x<y else print("no");

if __name__ == "__main__": main()
