#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(" Super Test", 42, 110);
    testfunc();

def testfunc(str=" default", num = 10, num2 = None):
    if num2 == None:
        num2=900;
    print('This is a test function' + str + " {}".format(num), num2);
    
#dummy function stub
def foo():
    pass;

if __name__ == "__main__": main()
