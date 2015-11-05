#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    a,b,c = 1,2,3;
    d = dict(x = 44, y = 12);
    
    print(s + " harro, {} {} {}".format(a,b,c));
    print(s + " harro, {1} {2} {0}".format(a,b,c));#format the order
    #assign value to the string
    print("this is {bomb} and this is {name}".format(bomb="cry", name="Stella"));
    print("this is {x} and this is {y}".format(**d));#apply key to dictionary
    #old format, c style
    print("harro, %d, %d" %(a,b));

if __name__ == "__main__": main()
