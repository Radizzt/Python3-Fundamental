#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    list =[];
    list = [0,1,2,3,4,5,6,7,8,9,10];
    
    print(list[0:5]);
    
    #shorthand to add 0-100 in a list
    list[:] = range(100);
    print(list);
    #slice from index 27 to 42
    print(list[27:42]);
    #slice from index 27 to 42 and every 3 steps
    print(list[27:42:3]);
    
    list[27:42:3] = (99,99,00,00,99);
    print(list);

if __name__ == "__main__": main()
