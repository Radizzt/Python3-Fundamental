#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c == 's': continue; #skip current loop and go to the next one
        print(c, end='')
    else:
        print(" else");#this will run when for loop is false (usually end of loop)
if __name__ == "__main__": main()
