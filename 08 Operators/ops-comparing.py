#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #has all common comparison operator, adding unique ones
    x,y= 1, 1#different ID
    print(x is y);#testing ID NOT values
    print(x is not y);
    x = y;
    print(x is y);
    

if __name__ == "__main__": main()
